#!/usr/bin/python


import time, os, pygame, random
from threading import Thread    ## import
from pygame.locals import *

from  technical import *


pi = 0 # 1 = running on pi, 0 = running in test mode
if os.path.exists("/dev/i2c-0"): # Am I runnin on a pi?
    pi = 1
    import smbus

if pi == 1:
    print "[INFO] Detected I2C. Running normally"
else:
    print "[INFO] Did not detect I2C. Running in simulation mode"

class fakeIIC():
    def read_word_data(self,a,b):
        return int(random.random()*65535)
    def write_byte_data(self,a,b,c):
        pass
    def write_word_data(self,a,b,c):
        pass

class IOThread(Thread):
    def __init__(self):  ## to pass a variable to the class add here
        Thread.__init__(self)
        self.pressure = 0
        self.distance = 0
        self.pgaSetting = 0x8060
        self.pressureAddress = 0x49 # Address of Pressure ADC
        self.distanceAddress = 0x48 # Address of Distance ADC (adddr hooked to vcc)
        self.ledAddresses = [0x60,0x61,0x62,0x63,0x64] # Addresses of LED 7 segment display Drivers
        self.bus = fakeIIC() # just init this in case something ties to use it.
        self.segmentLookup = [63, 6, 91, 79, 102, 109, 125, 7, 127, 111, 119, 124, 57, 94, 121, 113, 123]
        self.pressureArray = []
        self.lastPressure = 0
        self.lastDistance = 0
        self.Display = [0]*5
        self.pga = 1
        if pi == 1: # running on a Pi?
            self.bus = self.initI2C(self.pressureAddress,self.distanceAddress)
    def initI2C(self,pressureA,distanceA):
        bus = smbus.SMBus(1)# Setup IIC
        bus.write_word_data(pressureA,0x01,self.pgaSetting) # Default setup for Pressure
        bus.write_word_data(distanceA,0x01,self.pgaSetting) # Default setup for Distance
        #LEDS don't need setup
        return bus
    def pollpress(self):
        readingraw = convertReading(self.bus.read_word_data(self.pressureAddress,0x00))
        # if readingraw > 1000:
            # if self.pga == 2:
                # self.pga = 1
                # self.bus.write_word_data(self.pressureAddress,0x01,self.pgaSetting) # Gain of 2
            # elif self.pga == 4:
                # self.pga = 2
                # self.bus.write_word_data(self.pressureAddress,0x01,self.pgaSetting+2) # Gain of 4
            # readingraw = convertReading(self.bus.read_word_data(self.pressureAddress,0x00))
        # if readingraw < 500:
            # if self.pga == 1:
                # self.pga = 2
                # self.bus.write_word_data(self.pressureAddress,0x01,self.pgaSetting+2) # Gain of 2
            # elif self.pga == 2:
                # self.pga = 4
                # self.bus.write_word_data(self.pressureAddress,0x01,self.pgaSetting+4) # Gain of 4
            # readingraw = convertReading(self.bus.read_word_data(self.pressureAddress,0x00))
        pressure = readingraw/(2.0**self.pga)
        if pressure < 50000: 
                self.pressureArray.append([pressure,self.lastDistance,time.time()])#time.time is far away from reading, but should be ok
                return pressure
        else:
                return 0.0
    def setled(self,cellAddress,numberToDisplay):
        self.bus.write_byte_data(cellAddress, 0x44, self.segmentLookup[numberToDisplay])
    def getdist(self):
        readingraw = convertReading(self.bus.read_word_data(self.distanceAddress,0x00))
        distance = (readingraw-1200)/1200.0
        return distance
    def run(self):  ## dont need it here
        self.error = 0
        while self.error == 0:  ## Main thread program using passed variable
            self.lastPressure = self.pollpress()
            self.lastDistance = self.getdist()
            #print("Pressure",self.pressure)
            time.sleep(.0001)
            self.LED = 0
            #while (self.count < 5):
            #    self.pollpress()
            #    #self.setled(self.ledAddresses[self.LED],self.Display[self.LED])
            #    self.count += 1
            #    self.LED += 1
            #    #print("LED",self.LED)
            #    #print("distance",self.distance)
            #    time.sleep(.0057)



def Draw_Chart(surface,x,y,hsize,vsize,dataset,(DataStart,DataEnd),(DXMin,DXMax),(DYMin,DYMax),color,stroke,bordercolor,border):
    DataLen = DataEnd-DataStart
    DataHeightX = DXMax-DXMin
    DataHeightY = DYMax-DYMin
    xscale = (hsize+1)/DataLen
    xscale2 = (hsize)/DataHeightX
    yscale = -(vsize)/DataHeightY
    font = pygame.font.Font("freesansbold.ttf",12)
    if border >= 1:
        pygame.draw.lines(surface,bordercolor,0,((x,y),(x,y+vsize),(x+hsize,y+vsize),(x+hsize,y),(x,y)),border)
    lines = []
    if DataLen > hsize: #throw fit
        print "Not enough Graph Space. Impement a thingy."
        return
    for j in range(DataLen):
        i = dataset[j+DataStart]
        if (type(i)== type(float())) or (type(i) == type(int())):
            lines.append((x+(j*xscale),(y+vsize)-(i*yscale)))
        elif len(i) == 2:
            lines.append((x+((i[0]-DXMin)*xscale2),y+vsize+((i[1]-DYMin)*yscale)))
    pygame.draw.lines(surface,color,0,lines,stroke)
    pygame.draw.circle(surface,(0,0,255,128),(int(lines[-1][0]),int(lines[-1][1])),10)
    surface.blit(font.render("Data Width: "+str(DataHeightX)+" X Scale:"+str(xscale2)+" Y Scale:"+str(yscale),1,(100,255,100)),(40,80))
    try:
        surface.blit(font.render("Choords: "+str((float(lines[3][0]),float(lines[3][1]))),1,(100,255,100)),(40,100))
        surface.blit(font.render("Choords: "+str((float(dataset[3][0]),float(dataset[3][1]))),1,(100,255,100)),(40,120))
        surface.blit(font.render("Last: "+str((float(lines[-1][0]),float(lines[-1][1]))),1,(100,255,100)),(40,140))
        surface.blit(font.render("Last: "+str((float(dataset[-1][0]),float(dataset[-1][1]))),1,(100,255,100)),(40,160))
        surface.blit(font.render("Max: "+str((float(DXMax),float(DXMin),float(DYMax),float(DYMin))),1,(100,255,100)),(40,180))
    except:
        pass
    



def Main():
    ################ Pygame Init
    pygame.init()
    fpsclock = pygame.time.Clock()
    WindowSurface = pygame.display.set_mode((1400,800))
    pygame.display.set_caption("Pygame Test")
    
    
    ################# Pygame declarations
    #CustomImage = pygame.image.load("test.png")
    MouseSurface = pygame.Surface((32, 32), 0, 8).convert_alpha()
    MouseSurface.fill((0,100,0,0))
    pygame.draw.line(MouseSurface,(0,255,0),(16,0),(16,32),1)
    pygame.draw.line(MouseSurface,(0,255,0),(0,16),(32,16),1)
    
    font = pygame.font.Font("freesansbold.ttf",12)
    forceFont = pygame.font.Font("freesansbold.ttf",200)
    runProgram = 1
    mousex, mousey = 0,0
    lines = []
    Load = [0,50000]
    Dist = [0,50000]
    tp = 0.0
    td = 0.0
    PGA = 0
    while runProgram:
        WindowSurface.fill(pygame.Color(0,0,0)) # Screen Redraw
        # Process events
        for event in pygame.event.get():
            if event.type == QUIT:
                runProgram = 0
                break
            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    runProgram = 0
                    tclass.error = 1
                    break
                if event.key == K_UP:
                    tclass.pga = clamp(tclass.pga+1,1,5)
                    setting = tclass.pgaSetting +(tclass.pga*2)
                    print hex(setting)
                    #tclass.bus.write_word_data(tclass.distanceAddress,0x01,0x0000)
                    tclass.bus.write_word_data(tclass.pressureAddress,0x01,setting)
                if event.key == K_DOWN:
                    tclass.pga = clamp(tclass.pga-1,1,5)
                    setting = tclass.pgaSetting +(tclass.pga*2)
                    print hex(setting)
                    #tclass.bus.write_word_data(tclass.distanceAddress,0x01,0x0000)
                    tclass.bus.write_word_data(tclass.pressureAddress,0x01,setting)
                if event.key == K_RIGHT:
                    lines = []
                    Load = [0,50000]
                    Dist = [0,50000]
                    tp = 0.0
                    td = 0.0
                if event.key == K_LEFT:
                    print td
        readings = 0
        pressures = 0
        distances = 0
        while len(tclass.pressureArray) > 1:
            tmpAr = tclass.pressureArray.pop()
            readings += 1
            pressures += tmpAr[0]
            distances += tmpAr[1]
        if readings > 0:
            tp = pressures/readings #Averages
            td = distances/readings
            if tp > Load[0]:
                Load[0] = tp
            if tp < Load[1]:
                Load[1] = tp
            if td > Dist[0]:
                Dist[0] = td
            if td < Dist[1]:
                Dist[1] = td
            #print Dist, Load
            lines.append([td,tp])
        if len(lines)>2:
            Draw_Chart(WindowSurface,10,200,1380,590,lines,(0,len(lines)),(Dist[1],Dist[0]+.0001),(Load[1],Load[0]+.0001),(255,0,0),5,(255,255,255),3)
        
        #Draw
        WindowSurface.blit(MouseSurface,(mousex-16,mousey-16))
        WindowSurface.blit(forceFont.render(str(tp)[:5],1,(100,255,100)),(10,10))
        WindowSurface.blit(forceFont.render(str(td)[:5]+"\"",1,(100,255,100)),(700,10))
        #WindowSurface.blit(forceFont.render(str(hex(int(td*535)+1100))[:6]+"\"",1,(100,255,100)),(700,10))
        WindowSurface.blit(font.render("Max Load: "+str(60000/(2**tclass.pga))[:5]+"",1,(100,255,100)),(600,10))
        pygame.display.update()
        fpsclock.tick(10)
    pygame.quit()



tclass = IOThread() ## create instance
tclass.start() ## start class running



Main()






