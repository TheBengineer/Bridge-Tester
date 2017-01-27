#!/usr/bin/python


import os
import pygame
import random
import time
import serial
from pygame.locals import *
from threading import Thread  ## import

from  technical import *

pi = 0  # 1 = running on pi, 0 = running in test mode
if os.path.exists("/dev/i2c-0"):  # Am I runnin on a pi?
    pi = 1
    import smbus

if pi == 1:
    print "[INFO] Detected I2C. Running normally"
else:
    print "[INFO] Did not detect I2C. Running in simulation mode"


def log(*args):
    print "[Main]",
    # print time.strftime("%c"),
    # print " ",
    for arg in args:
        print arg,
    print ""


class fakeIIC():
    def read_word_data(self, a, b):
        return int(random.random() * 65535)

    def write_byte_data(self, a, b, c):
        pass

    def write_word_data(self, a, b, c):
        pass


class IOThread(Thread):
    def __init__(self):  ## to pass a variable to the class add here
        Thread.__init__(self)
        self.pressure = 0
        self.distance = 0
        self.PTare = 0
        self.DTare = 0
        self.pgaSetting = 0x8060
        self.pressureAddress = 0x49  # Address of Pressure ADC
        self.distanceAddress = 0x48  # Address of Distance ADC (adddr hooked to vcc)
        self.ledAddresses = [0x60, 0x61, 0x62, 0x63, 0x64]  # Addresses of LED 7 segment display Drivers
        self.bus = fakeIIC()  # just init this in case something ties to use it.
        self.segmentLookup = [63, 6, 91, 79, 102, 109, 125, 7, 127, 111, 119, 124, 57, 94, 121, 113, 123]
        self.pressureArray = []
        self.lastPressure = 0
        self.lastDistance = 0
        self.Display = [0] * 5
        self.fps = 0
        self.lasttime = time.time()
        self.calibration = 0.929373554
        self.calibrationOffset = 46
        self.force_serial = None
        if pi == 1:  # running on a Pi?
            self.bus = self.initI2C(self.pressureAddress, self.distanceAddress)

    def initI2C(self, pressureA, distanceA):
        bus = smbus.SMBus(1)  # Setup IIC
        bus.write_word_data(pressureA, 0x01, self.pgaSetting)  # Default setup for Pressure
        bus.write_word_data(distanceA, 0x01, self.pgaSetting)  # Default setup for Distance
        # LEDS don't need setup
        self.connect_USBs()
        return bus

    @staticmethod
    def find_all_USBs():
        """
        This function finds all connected USB sensors
        :return: Returns a list of strings, EG: 'ttyUSB0'
        """
        return [dev for dev in os.listdir("/dev/") if dev.startswith("ttyUSB")]

    def connect_USBs(self):
        """
        Opens a serial stream to the sensors, and tries to determine which is which.
        Streams are stored to local variables
        """
        all_devs = self.find_all_USBs()  # Get all USB devices to scan
        # Make sure there are 2 connected
        if len(all_devs) == 0:
            log("[ERROR] There are no detected sensors")
            raise IOError
        elif len(all_devs) == 1:
            log("[ OK ] One sensor connected at '/dev/{}'.".format(all_devs[0]))
            raise IOError
        elif len(all_devs) > 2:
            log("[WARNING] More than one sensor detected. Will try to determine which sensors to use.\n\tSensors:{}".format(all_devs))

        # Check all devices to figure out which is force, and which is displacement.
        for dev in all_devs:
            baud = 115200
            self.force_serial = serial.Serial(port='/dev/' + dev, baudrate=baud)
            if not self.force_serial.isOpen():
                self.force_serial.open()
            self.force_serial.write("RATE 8\n\r")

    def pollpress(self):
        if not self.force_serial:
            log("No force sensor detected.")
            raise IOError
        self.force_serial.write("P\n\r")
        self.force_serial.flush()
        time.sleep(.01)
        msg = ""
        while self.force_serial.inWaiting():
            msg += self.force_serial.read(1)
        reading_raw = msg[0:msg.find("P")]
        try:
            pressure = float(reading_raw)
        except ValueError:
            pressure = None

        pressure -= self.PTare

        if pressure is not None:
            self.pressureArray.append([pressure, self.lastDistance])  # time.time is far away from reading, but should be ok
        return pressure

    def pollpress2(self):
        readingraw = convertReading(self.bus.read_word_data(self.pressureAddress, 0x00))
        pressure = readingraw * self.calibration
        pressure += -self.PTare + self.calibrationOffset
        self.pressureArray.append((pressure, self.lastDistance))
        return pressure

    def setled(self, cellAddress, numberToDisplay):
        self.bus.write_byte_data(cellAddress, 0x44, self.segmentLookup[numberToDisplay])

    def getdist(self):
        readingraw = convertReading(self.bus.read_word_data(self.distanceAddress, 0x00))
        distance = (readingraw - 1200) / 1200.0
        distance -= self.DTare
        return distance

    def run(self):  ## dont need it here
        self.error = 0
        self.polls = 0
        self.lastDistance = self.getdist()
        while self.error == 0:  ## Main thread program using passed variable
            self.lastPressure = self.pollpress()
            if self.polls % 10 == 0:
                self.lastDistance = self.getdist()
            self.polls += 1
            time.sleep(.001)


def Draw_Chart(surface, x, y, hsize, vsize, dataset, (DataStart, DataEnd), (DXMin, DXMax), (DYMin, DYMax), color, stroke, bordercolor, border, stringFormat,
               stringFormat2, MLfont):
    DataLen = DataEnd - DataStart
    DataHeightX = DXMax - DXMin
    DataHeightY = DYMax - DYMin
    xscale = (hsize + 1) / DataLen
    xscale2 = (hsize) / DataHeightX
    yscale = -(vsize - 25) / DataHeightY
    maxVal = 0
    maxInd = 0
    pygame.draw.rect(surface, (0, 0, 0), (x - 25, y, hsize + 50, vsize + 25))
    if border >= 1:
        draw_rect(surface, (x, y, hsize, vsize), bordercolor, 25, 3)
    lines = []
    for j in range(DataLen):
        i = dataset[j + DataStart]
        if i[1] > maxVal:
            maxVal = i[1]
            maxInd = j
        lines.append((x + ((i[0] - DXMin) * xscale2), y + vsize + ((i[1] - DYMin) * yscale)))
    pygame.draw.lines(surface, color, 0, lines, stroke)
    c = (255, 255, 255)
    tc = (255, 0, 0)
    px, py = (x + ((dataset[maxInd][0] - DXMin) * xscale2), y + vsize + ((dataset[maxInd][1] - DYMin) * yscale))
    if px > hsize / 2:
        draw_tag2(surface, (px, py), 1, c, tc, MLfont, stringFormat.format(dataset[maxInd][1]), stringFormat2.format(dataset[maxInd][0]))
    else:
        draw_tag2(surface, (px, py), 0, c, tc, MLfont, stringFormat.format(dataset[maxInd][1]), stringFormat2.format(dataset[maxInd][0]))
    tc = (0, 100, 255)
    px, py = (x + ((dataset[-1][0] - DXMin) * xscale2), y + vsize + ((dataset[-1][1] - DYMin) * yscale))
    if px > hsize / 2:
        draw_tag(surface, (px, py), 1, c, tc, MLfont, stringFormat.format(dataset[-1][1]))
    else:
        draw_tag(surface, (px, py), 0, c, tc, MLfont, stringFormat.format(dataset[-1][1]))


def draw_rect(surface, (x, y, w, h), color, cx, width):
    lines = (
    (x + cx, y), (x + w - cx, y), (x + w, y + cx), (x + w, y + h - cx), (x + w - cx, y + h), (x + cx, y + h), (x, y + h - cx), (x, y + cx), (x + cx, y))
    pygame.draw.lines(surface, color, 0, lines, width)


def draw_tag(surface, (x, y), left, color, tcolor, font, string):
    tag = [(x + 20, y), (x, y - 20), (x - 20, y), (x, y + 20), (x + 20, y)]
    if left == 1:
        tx, ty = x - 220, y
        pygame.draw.lines(surface, color, 0, ((x - 20, y), (tx + 150, ty)), 2)
    else:
        tx, ty = x + 220, y
        pygame.draw.lines(surface, color, 0, ((x + 20, y), (tx - 150, ty)), 2)
    tag2 = [(tx + 150, ty), (tx + 130, ty - 20), (tx - 130, ty - 20), (tx - 150, ty), (tx - 130, ty + 20), (tx + 130, ty + 20), (tx + 150, ty)]
    pygame.draw.lines(surface, color, 0, tag, 2)
    pygame.draw.lines(surface, color, 0, tag2, 2)
    pygame.draw.lines(surface, color, 0, ((tx, ty - 20), (tx - 130, ty - 20)), 2)
    surface.blit(font.render(string, 1, tcolor), (tx - 130, ty - 14))


def draw_tag2(surface, (x, y), left, color, tcolor, font, string, string2):
    tag = [(x + 20, y), (x, y - 20), (x - 20, y), (x, y + 20), (x + 20, y)]
    if left == 1:
        tx, ty = x - 220, y
        pygame.draw.lines(surface, color, 0, ((x - 20, y), (tx + 150, ty)), 2)
    else:
        tx, ty = x + 220, y
        pygame.draw.lines(surface, color, 0, ((x + 20, y), (tx - 150, ty)), 2)
    tag2 = [(tx + 150, ty), (tx + 130, ty - 20), (tx - 130, ty - 20), (tx - 150, ty), (tx - 130, ty + 20), (tx + 130, ty + 20), (tx + 150, ty)]
    tag3 = [(tx + 130, ty + 20), (tx + 150, ty + 40), (tx + 130, ty + 60), (tx - 130, ty + 60), (tx - 150, ty + 40), (tx - 130, ty + 20)]
    pygame.draw.lines(surface, color, 0, tag, 2)
    pygame.draw.lines(surface, color, 0, tag2, 2)
    pygame.draw.lines(surface, color, 0, tag3, 2)
    pygame.draw.lines(surface, color, 0, ((tx, ty - 20), (tx - 130, ty - 20)), 2)
    surface.blit(font.render(string, 1, tcolor), (tx - 130, ty - 14))
    surface.blit(font.render(string2, 1, tcolor), (tx - 130, ty + 26))


def Main():
    ################ Pygame Init
    pygame.init()
    fpsclock = pygame.time.Clock()
    WindowSurface = pygame.display.set_mode((1918, 1078), pygame.FULLSCREEN)
    pygame.display.set_caption("Pygame Test")
    pygame.mouse.set_visible(0)
    fps = 0

    ################# Pygame declarations
    # CustomImage = pygame.image.load("test.png")
    MouseSurface = pygame.Surface((32, 32), 0, 8).convert_alpha()
    MouseSurface.fill((0, 100, 0, 0))
    pygame.draw.line(MouseSurface, (0, 255, 0), (16, 0), (16, 32), 1)
    pygame.draw.line(MouseSurface, (0, 255, 0), (0, 16), (32, 16), 1)
    font = pygame.font.Font("freesansbold.ttf", 12)
    forceFont = pygame.font.Font("freesansbold.ttf", 200)
    MLfont = pygame.font.Font("freesansbold.ttf", 30)
    GTfont = pygame.font.Font("freesansbold.ttf", 75)
    Gfont = pygame.font.Font("freesansbold.ttf", 60)
    AxisFont = pygame.font.Font("freesansbold.ttf", 10)
    ######### Static Draw
    displacementLimit = 2.1
    loadOver = 0

    draw_rect(WindowSurface, (10, 40, 1180, 175), (0, 100, 250), 25, 3)  # max load
    WindowSurface.blit(forceFont.render("MAX LOAD", 1, (255, 255, 255)), (72, 20))
    draw_rect(WindowSurface, (1205, 40, 700, 175), (0, 100, 250), 25, 3)  # displacement
    WindowSurface.blit(forceFont.render("FLEX", 1, (255, 255, 255)), (1300, 20))
    WindowSurface.blit(forceFont.render("LB", 1, (255, 0, 0)), (900, 210))

    draw_rect(WindowSurface, (10, 230, 1180, 175), (0, 100, 250), 25, 3)  # Load Rect
    draw_rect(WindowSurface, (1205, 230, 700, 175), (0, 100, 250), 25, 3)  # displacement Rect

    draw_rect(WindowSurface, (1205, 420, 700, 625), (0, 100, 250), 25, 3)  # Dedication Rect
    WindowSurface.blit(Gfont.render("Dedicated To", 1, (255, 255, 255)), (1380, 420))  # Reynolds
    WindowSurface.blit(GTfont.render("Gordon Reynolds", 1, (255, 255, 255)), (1240, 480))  # Reynolds
    WindowSurface.blit(Gfont.render("For his many years of", 1, (255, 255, 255)), (1245, 620))  # Reynolds
    WindowSurface.blit(Gfont.render("outstanding service", 1, (255, 255, 255)), (1275, 680))  # Reynolds
    WindowSurface.blit(Gfont.render("for the students of", 1, (255, 255, 255)), (1295, 740))  # Reynolds
    WindowSurface.blit(Gfont.render("Vermont Technical", 1, (255, 255, 255)), (1290, 840))  # Reynolds
    WindowSurface.blit(Gfont.render("College", 1, (255, 255, 255)), (1445, 900))  # Reynolds

    runProgram = 1
    time.sleep(.5)  # warmup
    lines = []
    loadOver = 0
    Load = [0, 50000]
    Dist = [0, 50000]
    tclass.DTare = tclass.lastDistance + tclass.DTare
    tclass.PTare = tclass.lastPressure + tclass.PTare
    tp = 0.0
    td = 0.0
    time.sleep(.1)
    tclass.pressureArray = []  # clear saved pressures
    PullNum = 0

    while runProgram:
        # WindowSurface.fill(pygame.Color(0,0,0)) # Screen Redraw
        # Process events
        for event in pygame.event.get():
            if event.type == QUIT:
                runProgram = 0
                break
            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            if event.type == KEYDOWN:
                if event.scancode == 123:
                    displacementLimit += .1
                    pygame.draw.rect(WindowSurface, (0, 0, 0), (160, 480, 820, 110))  # Draw Black
                    draw_rect(WindowSurface, (170, 490, 800, 90), (0, 100, 250), 25, 3)  # max load
                    WindowSurface.blit(Gfont.render("Max Deflection: {0:.3f}\"".format(displacementLimit), 1, (255, 200, 0)), (200, 500))  # Saving
                    pygame.display.update()
                    time.sleep(.2)
                if event.scancode == 122:
                    displacementLimit -= .1
                    pygame.draw.rect(WindowSurface, (0, 0, 0), (160, 480, 820, 110))  # Draw Black
                    draw_rect(WindowSurface, (170, 490, 800, 90), (0, 100, 250), 25, 3)  # max load
                    WindowSurface.blit(Gfont.render("Max Deflection: {0:.3f}\"".format(displacementLimit), 1, (255, 200, 0)), (200, 500))  # Saving
                    pygame.display.update()
                    time.sleep(.2)
                if event.key == K_ESCAPE or event.key == K_7:
                    runProgram = 0
                    tclass.error = 1
                    os.system("sudo shutdown now")
                    break
                if event.key == K_q:
                    runProgram = 0
                    tclass.error = 1
                    break
                if event.key == K_d:
                    WindowSurface.blit(Gfont.render("Dedicated To", 1, (255, 255, 255)), (1380, 420))  # Reynolds
                    WindowSurface.blit(GTfont.render("Gordon Reynolds", 1, (255, 255, 255)), (1240, 480))  # Reynolds
                    WindowSurface.blit(Gfont.render("For his many years of", 1, (255, 255, 255)), (1245, 620))  # Reynolds
                    WindowSurface.blit(Gfont.render("outstanding service", 1, (255, 255, 255)), (1275, 680))  # Reynolds
                    WindowSurface.blit(Gfont.render("for the students of", 1, (255, 255, 255)), (1295, 740))  # Reynolds
                    WindowSurface.blit(Gfont.render("Vermont Technical", 1, (255, 255, 255)), (1290, 840))  # Reynolds
                    WindowSurface.blit(Gfont.render("College", 1, (255, 255, 255)), (1445, 900))  # Reynolds
                if event.key == K_e or event.key == K_SPACE:
                    if Load[0] > 30:
                        sbak = WindowSurface.copy()
                        draw_rect(WindowSurface, (170, 490, 400, 90), (0, 100, 250), 25, 3)  # max load
                        WindowSurface.blit(Gfont.render("Saving Data", 1, (255, 255, 255)), (200, 500))  # Saving
                        pygame.display.update()
                        try:
                            for directories in os.listdir("/media/"):
                                if directories != "SETTINGS SD" and directories != "SETTINGS" and directories != "BOOT":
                                    wd = "/media/" + directories
                                    print "Saving Pull data to ", wd
                                    try:
                                        config = open(wd + "/Gordonator.txt", 'r')
                                        PullNum = int(config.read())
                                        config.close()
                                    except:
                                        pass
                                    fn = wd + "/Crush " + str(PullNum)
                                    print "under files:", fn + ".jpg , ", fn + ".csv"
                                    pygame.image.save(sbak, fn + ".jpg")
                                    csv = open(fn + ".csv", 'w')
                                    csv.write("Gordonator crush data for crush #" + str(PullNum) + "\n")
                                    csv.write("Deflection,Load\n")
                                    for dp in lines:
                                        csv.write(str(dp[0]) + "," + str(dp[1]) + "\n")
                                    csv.close()
                                    PullNum += 1
                                    config = open(wd + "/Gordonator.txt", 'w')
                                    config.write(str(PullNum))
                                    config.close()
                                else:
                                    print "No flash Drive detected. Saving failed"
                        except:
                            print "Saving to flash drive failed"
                    lines = []
                    loadOver = 0
                    Load = [0, 50000]
                    Dist = [0, 50000]
                    tclass.DTare = tclass.lastDistance + tclass.DTare
                    tclass.PTare = tclass.lastPressure + tclass.PTare
                    tp = 0.0
                    td = 0.0
                    time.sleep(.1)
                    pygame.draw.rect(WindowSurface, (0, 0, 0), (0, 420, 1230, 700))  # Draw Black
                    tclass.pressureArray = []  # clear saved pressures
        while len(tclass.pressureArray) > 11:
            readings = 0
            pressures = 0
            maxPressure = 0
            distances = 0
            for i in range(10):
                tmpAr = tclass.pressureArray.pop(0)
                readings += 1
                pressures += tmpAr[0]
                distances += tmpAr[1]
                maxPressure = max(tmpAr[0], maxPressure)
            if readings > 0:
                tp = pressures / readings  # Averages
                # tp = maxPressure #Max
                td = distances / readings
                if tp > Load[0]:
                    Load[0] = tp
                if tp < Load[1]:
                    Load[1] = tp
                if td > Dist[0]:
                    Dist[0] = td
                if td < Dist[1]:
                    Dist[1] = td
                # print Dist, Load
                # if tp > 1: # This is messy
                lines.append([td, tp])
                # linesAvg.append([td,pressures/readings])
                # lines.append([td,pressures/readings]) # Averaging
                if td > displacementLimit and loadOver == 0:
                    loadOver = Load[0]

        pygame.draw.rect(WindowSurface, (0, 0, 0), (0, 420, 1230, 675))  # Draw Black
        if len(lines) > 2:
            timev = time.time()
            # charttimes = Draw_Chart(WindowSurface,10,420,1180,600,lines,(0,len(lines)),(Dist[1],clamp(Dist[0],Dist[1]+.05,300000)),(Load[1],clamp(Load[0],Load[1]+80,300000)),(255,255,255),1,(0,100,255),3,"{0:.2f} LB","{0:.3f}\"",MLfont)
            # Draw_Chart(surface,x,y,hsize,vsize,dataset,(DataStart,DataEnd),(DXMin,DXMax),(DYMin,DYMax),color,stroke,bordercolor,border,stringFormat,stringFormat2,MLfont):
            DataLen = len(lines)
            DataHeightX = clamp(Dist[0], Dist[1] + .05, 300000) - Dist[1]
            DataHeightY = clamp(Load[0], Load[1] + 80, 300000) - Load[1]
            xscale2 = 1180 / DataHeightX
            yscale = -575 / DataHeightY
            maxVal = 0
            maxInd = 0
            pygame.draw.rect(WindowSurface, (0, 0, 0), (0, 420, 1230, 625))  # Draw Black
            ######### Boarder
            # pygame.draw.lines(WindowSurface,(0,100,255),0,((35, 420), (1165, 420), (1190, 445), (1190, 995), (1165, 1020), (35, 1020), (10, 995), (10, 445), (35, 420)),3)
            pygame.draw.lines(WindowSurface, (0, 100, 255), 0,
                              ((35, 420), (1165, 420), (1190, 445), (1190, 1020), (1165, 1046), (35, 1046), (10, 1020), (10, 445), (35, 420)), 3)
            scaled = []
            ################ Compute Scale
            j = 0
            while j < len(lines):
                if lines[j][1] > maxVal:
                    maxVal = lines[j][1]
                    maxInd = j
                scaled.append((10 + ((lines[j][0] - Dist[1]) * xscale2), 1020 + ((lines[j][1] - Load[1]) * yscale)))
                j += 1
            pygame.draw.lines(WindowSurface, (255, 255, 255), 0, scaled, 1)
            px, py = (10 + ((lines[maxInd][0] - Dist[1]) * xscale2), 1020 + ((lines[maxInd][1] - Load[1]) * yscale))
            if px > 600:  # "{0:.2f} LB","{0:.3f}\""
                draw_tag2(WindowSurface, (px, py), 1, (255, 255, 255), (255, 0, 0), MLfont, "{0:.2f} LB".format(lines[maxInd][1]),
                          "{0:.3f}\"".format(lines[maxInd][0]))
            else:
                draw_tag2(WindowSurface, (px, py), 0, (255, 255, 255), (255, 0, 0), MLfont, "{0:.2f} LB".format(lines[maxInd][1]),
                          "{0:.3f}\"".format(lines[maxInd][0]))
            px, py = (10 + ((lines[-1][0] - Dist[1]) * xscale2), 1020 + ((lines[-1][1] - Load[1]) * yscale))
            if px > 600:
                draw_tag(WindowSurface, (px, py), 1, (255, 255, 255), (0, 100, 255), MLfont, "{0:.2f} LB".format(lines[-1][1]))
            else:
                draw_tag(WindowSurface, (px, py), 0, (255, 255, 255), (0, 100, 255), MLfont, "{0:.2f} LB".format(lines[-1][1]))
            if loadOver > 0:
                px, py = (10 + ((displacementLimit - Dist[1]) * xscale2), 1020 + ((loadOver - Load[1]) * yscale))
                if px > 600:
                    draw_tag2(WindowSurface, (px, py), 1, (255, 255, 255), (255, 200, 0), MLfont, "{0:.2f} LB".format(loadOver),
                              "{0:.3f}\"".format(displacementLimit))
                else:
                    draw_tag2(WindowSurface, (px, py), 0, (255, 255, 255), (255, 200, 0), MLfont, "{0:.2f} LB".format(loadOver),
                              "{0:.3f}\"".format(displacementLimit))
            if DataHeightY > 50000:
                limit = 5000
            if DataHeightY > 10000:
                limit = 1000
            elif DataHeightY > 5000:
                limit = 500
            elif DataHeightY > 1000:
                limit = 100
            else:
                limit = 50
            ######## Vertical Graph
            i = Load[1] + (limit - (Load[1] % limit))
            pygame.draw.line(WindowSurface, (0, 255, 0), [13, 1020], [25, 1020])
            WindowSurface.blit(AxisFont.render("{:>5.0f} LB".format(Load[1]), 1, (0, 255, 0)), (25, 1015))  # Bottom label
            while i < Load[0]:
                pixy = 1020 + ((i - Load[1]) * yscale)
                pygame.draw.line(WindowSurface, (0, 255, 0), [13, pixy], [25, pixy])
                WindowSurface.blit(AxisFont.render("{:>5.0f} LB".format(i), 1, (0, 255, 0)), (25, pixy - 5))  # Axis labels
                i += limit
            ######## Horizontal Graph
            i = Dist[1] + (.5 - (Dist[1] % .5))
            pygame.draw.line(WindowSurface, (0, 255, 0), [10, 1020], [10, 1035])
            a = 0
            while i < Dist[0]:
                pixx = 10 + ((i - Dist[1]) * xscale2)
                pygame.draw.line(WindowSurface, (0, 255, 0), [pixx, 1026], [pixx, 1035 + a])
                WindowSurface.blit(AxisFont.render("{:>2.1f}\"".format(i), 1, (0, 255, 0)), (pixx - 10, 1037 + a))  # Axis labels
                i += .5
                a = (a + 15) % 30
            WindowSurface.blit(AxisFont.render("{:>2.1f}\"".format(Dist[1]), 1, (0, 255, 0)), (0, 1052))  # Bottom label
        else:
            pygame.draw.lines(WindowSurface, (0, 100, 255), 0,
                              ((35, 420), (1165, 420), (1190, 445), (1190, 1020), (1165, 1046), (35, 1046), (10, 1020), (10, 445), (35, 420)), 3)

        pygame.draw.rect(WindowSurface, (0, 0, 0), (35, 235, 820, 165))  # Blank load
        WindowSurface.blit(forceFont.render("{:>9.0f}".format(Load[0]), 1, (255, 0, 0)), (10, 210))  # Load
        pygame.draw.rect(WindowSurface, (0, 0, 0), (1230, 235, 650, 165))  # Blank Displacement. This line may need tweaking.
        WindowSurface.blit(forceFont.render("{0:>7.2f}\"".format(td), 1, (255, 0, 0)), (1175, 210))  # Displacement

        pygame.draw.lines(WindowSurface, (0, 100, 255), 0, ((1230, 1045), (1205, 1020), (1205, 445), (1230, 420)), 3)  # Fix overwrite

        pygame.display.update()
    # f.close()
    pygame.quit()


timev = 0

tclass = IOThread()  ## create instance
tclass.start()  ## start class running

Main()
