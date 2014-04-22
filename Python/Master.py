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
        self.PTare = 0
        self.DTare = 0
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
        self.fps = 0
        self.lasttime = time.time()
        self.calibration = 0.929373554
        self.calibrationOffset = 26
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
        pressure = readingraw*self.calibration
        pressure += -self.PTare + self.calibrationOffset
        self.pressureArray.append((pressure,self.lastDistance))
        return pressure
    def setled(self,cellAddress,numberToDisplay):
        self.bus.write_byte_data(cellAddress, 0x44, self.segmentLookup[numberToDisplay])
    def getdist(self):
        readingraw = convertReading(self.bus.read_word_data(self.distanceAddress,0x00))
        distance = (readingraw-1200)/1200.0
        distance -= self.DTare
        return distance
    def run(self):  ## dont need it here
        self.error = 0
        self.polls = 0
        self.lastDistance = self.getdist()
        while self.error == 0:  ## Main thread program using passed variable
            self.lastPressure = self.pollpress()
            if self.polls%10 == 0:
                self.lastDistance = self.getdist()
            self.polls += 1
            time.sleep(.001)



def Draw_Chart(surface,x,y,hsize,vsize,dataset,(DataStart,DataEnd),(DXMin,DXMax),(DYMin,DYMax),color,stroke,bordercolor,border,stringFormat,stringFormat2,MLfont):
    DataLen = DataEnd-DataStart
    DataHeightX = DXMax-DXMin
    DataHeightY = DYMax-DYMin
    xscale = (hsize+1)/DataLen
    xscale2 = (hsize)/DataHeightX
    yscale = -(vsize-25)/DataHeightY
    maxVal = 0
    maxInd = 0
    pygame.draw.rect(surface,(0,0,0),(x-25,y,hsize+50,vsize+25))
    if border >= 1:
        draw_rect(surface,(x,y,hsize,vsize),bordercolor,25,3)
    lines = []
    for j in range(DataLen):
        i = dataset[j+DataStart]
        if i[1] > maxVal:
            maxVal = i[1]
            maxInd = j
        lines.append((x+((i[0]-DXMin)*xscale2),y+vsize+((i[1]-DYMin)*yscale)))
    pygame.draw.lines(surface,color,0,lines,stroke)
    c = (255,255,255)
    tc = (255,0,0)
    px,py = (x+((dataset[maxInd][0]-DXMin)*xscale2),y+vsize+((dataset[maxInd][1]-DYMin)*yscale))
    if px > hsize/2:
        draw_tag2(surface,(px,py),1,c,tc,MLfont,stringFormat.format(dataset[maxInd][1]),stringFormat2.format(dataset[maxInd][0]))
    else:
        draw_tag2(surface,(px,py),0,c,tc,MLfont,stringFormat.format(dataset[maxInd][1]),stringFormat2.format(dataset[maxInd][0]))
    tc = (0,100,255)
    px,py = (x+((dataset[-1][0]-DXMin)*xscale2),y+vsize+((dataset[-1][1]-DYMin)*yscale))
    if px > hsize/2:
        draw_tag(surface,(px,py),1,c,tc,MLfont,stringFormat.format(dataset[-1][1]))
    else:
        draw_tag(surface,(px,py),0,c,tc,MLfont,stringFormat.format(dataset[-1][1]))
    
def draw_rect(surface,(x,y,w,h),color,cx,width):
    lines = ((x+cx,y),(x+w-cx,y),(x+w,y+cx),(x+w,y+h-cx),(x+w-cx,y+h),(x+cx,y+h),(x,y+h-cx),(x,y+cx),(x+cx,y))
    pygame.draw.lines(surface,color,0,lines,width)
def draw_tag(surface,(x,y),left,color,tcolor,font,string):
    tag = [(x+20,y),(x,y-20),(x-20,y),(x,y+20),(x+20,y)]
    if left == 1:
        tx,ty = x-220,y
        pygame.draw.lines(surface,color,0,((x-20,y),(tx+150,ty)),2)
    else:
        tx,ty = x+220,y
        pygame.draw.lines(surface,color,0,((x+20,y),(tx-150,ty)),2)
    tag2 = [(tx+150,ty),(tx+130,ty-20),(tx-130,ty-20),(tx-150,ty),(tx-130,ty+20),(tx+130,ty+20),(tx+150,ty)]
    pygame.draw.lines(surface,color,0,tag,2)
    pygame.draw.lines(surface,color,0,tag2,2)
    pygame.draw.lines(surface,color,0,((tx,ty-20),(tx-130,ty-20)),2)
    surface.blit(font.render(string,1,tcolor),(tx-130,ty-14))
    
def draw_tag2(surface,(x,y),left,color,tcolor,font,string,string2):
    tag = [(x+20,y),(x,y-20),(x-20,y),(x,y+20),(x+20,y)]
    if left == 1:
        tx,ty = x-220,y
        pygame.draw.lines(surface,color,0,((x-20,y),(tx+150,ty)),2)
    else:
        tx,ty = x+220,y
        pygame.draw.lines(surface,color,0,((x+20,y),(tx-150,ty)),2)
    tag2 = [(tx+150,ty),(tx+130,ty-20),(tx-130,ty-20),(tx-150,ty),(tx-130,ty+20),(tx+130,ty+20),(tx+150,ty)]
    tag3 = [(tx+130,ty+20),(tx+150,ty+40),(tx+130,ty+60),(tx-130,ty+60),(tx-150,ty+40),(tx-130,ty+20)]
    pygame.draw.lines(surface,color,0,tag,2)
    pygame.draw.lines(surface,color,0,tag2,2)
    pygame.draw.lines(surface,color,0,tag3,2)
    pygame.draw.lines(surface,color,0,((tx,ty-20),(tx-130,ty-20)),2)
    surface.blit(font.render(string,1,tcolor),(tx-130,ty-14))
    surface.blit(font.render(string2,1,tcolor),(tx-130,ty+26))
    
def Main():
    ################ Pygame Init
    pygame.init()
    fpsclock = pygame.time.Clock()
    WindowSurface = pygame.display.set_mode((1918,1078))#,pygame.FULLSCREEN)
    pygame.display.set_caption("Pygame Test")
    fps = 0
    
    ################# Pygame declarations
    #CustomImage = pygame.image.load("test.png")
    MouseSurface = pygame.Surface((32, 32), 0, 8).convert_alpha()
    MouseSurface.fill((0,100,0,0))
    pygame.draw.line(MouseSurface,(0,255,0),(16,0),(16,32),1)
    pygame.draw.line(MouseSurface,(0,255,0),(0,16),(32,16),1)
    font = pygame.font.Font("freesansbold.ttf",12)
    forceFont = pygame.font.Font("freesansbold.ttf",200)
    MLfont = pygame.font.Font("freesansbold.ttf",30)
    GTfont = pygame.font.Font("freesansbold.ttf",75)
    Gfont = pygame.font.Font("freesansbold.ttf",60)
    ######### Static Draw
    
    draw_rect(WindowSurface,(10,40,1180,175),(0,100,250),25,3) # max load
    WindowSurface.blit(forceFont.render("MAX LOAD",1,(255,255,255)),(72,20))
    draw_rect(WindowSurface,(1205,40,700,175),(0,100,250),25,3)# displacement
    WindowSurface.blit(forceFont.render("FLEX",1,(255,255,255)),(1300,20))
    WindowSurface.blit(forceFont.render("LB",1,(255,0,0)),(900,210))
    
    draw_rect(WindowSurface,(10,230,1180,175),(0,100,250),25,3) #Load Rect
    draw_rect(WindowSurface,(1205,230,700,175),(0,100,250),25,3)# displacement Rect
    
    draw_rect(WindowSurface,(1205,420,700,600),(0,100,250),25,3)# displacement Rect
    #WindowSurface.blit(Gfont.render("Dedicated To",1,(255,255,255)),(1380,420))# Reynolds
    #WindowSurface.blit(GTfont.render("Gordon Reynolds",1,(255,255,255)),(1240,480))# Reynolds
    #WindowSurface.blit(Gfont.render("For his many years of",1,(255,255,255)),(1245,620))# Reynolds
    #WindowSurface.blit(Gfont.render("outstanding service",1,(255,255,255)),(1275,680))# Reynolds
    #WindowSurface.blit(Gfont.render("for the students of",1,(255,255,255)),(1295,740))# Reynolds
    #WindowSurface.blit(Gfont.render("Vermont Technical",1,(255,255,255)),(1290,840))# Reynolds
    #WindowSurface.blit(Gfont.render("College",1,(255,255,255)),(1445,900))# Reynolds


    runProgram = 1
    mousex, mousey = 0,0
    lines = []
    Load = [0,50000]
    Dist = [0,50000]
    tp = 0.0
    td = 0.0
    PGA = 0
    #f = open("/home/ben/Bridge_Tester/Python/times.csv","w")
    while runProgram:
        #WindowSurface.fill(pygame.Color(0,0,0)) # Screen Redraw
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
                if event.key == K_RIGHT:
                    lines = []
                    Load = [0,50000]
                    Dist = [0,50000]
                    tclass.DTare = tclass.lastDistance+tclass.DTare
                    tclass.PTare = tclass.lastPressure+tclass.PTare
                    tp = 0.0
                    td = 0.0
                    time.sleep(.1)
                    tclass.pressureArray = [] # clear saved pressures
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
                maxPressure = max(tmpAr[0],maxPressure)
            if readings > 0:
                #tp = pressures/readings #Averages
                tp = maxPressure #Max
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
            timev = time.time()
            #charttimes = Draw_Chart(WindowSurface,10,420,1180,600,lines,(0,len(lines)),(Dist[1],clamp(Dist[0],Dist[1]+.05,300000)),(Load[1],clamp(Load[0],Load[1]+80,300000)),(255,255,255),1,(0,100,255),3,"{0:.2f} LB","{0:.3f}\"",MLfont)
            # Draw_Chart(surface,x,y,hsize,vsize,dataset,(DataStart,DataEnd),(DXMin,DXMax),(DYMin,DYMax),color,stroke,bordercolor,border,stringFormat,stringFormat2,MLfont):
            DataLen = len(lines)
            DataHeightX = clamp(Dist[0],Dist[1]+.05,300000)-Dist[1]
            DataHeightY = clamp(Load[0],Load[1]+.05,300000)-Load[1]
            xscale2 = 1180/DataHeightX
            yscale = -575/DataHeightY
            maxVal = 0
            maxInd = 0
            pygame.draw.rect(WindowSurface,(0,0,0),(0,420,1230,625)) # Draw Black
            pygame.draw.lines(WindowSurface,(0,100,255),0,((35, 420), (1165, 420), (1190, 445), (1190, 995), (1165, 1020), (35, 1020), (10, 995), (10, 445), (35, 420)),3)
            scaled = []
            # for j in range(DataLen):
                # i = dataset[j+DataStart]
                # if i[1] > maxVal:
                    # maxVal = i[1]
                    # maxInd = j
                # lines.append((x+((i[0]-DXMin)*xscale2),y+vsize+((i[1]-DYMin)*yscale)))
            # pygame.draw.lines(surface,color,0,lines,stroke)
            # c = (255,255,255)
            # tc = (255,0,0)
            # px,py = (x+((dataset[maxInd][0]-DXMin)*xscale2),y+vsize+((dataset[maxInd][1]-DYMin)*yscale))
            # if px > hsize/2:
                # draw_tag2(surface,(px,py),1,c,tc,MLfont,stringFormat.format(dataset[maxInd][1]),stringFormat2.format(dataset[maxInd][0]))
            # else:
                # draw_tag2(surface,(px,py),0,c,tc,MLfont,stringFormat.format(dataset[maxInd][1]),stringFormat2.format(dataset[maxInd][0]))
            # tc = (0,100,255)
            # px,py = (x+((dataset[-1][0]-DXMin)*xscale2),y+vsize+((dataset[-1][1]-DYMin)*yscale))
            # if px > hsize/2:
                # draw_tag(surface,(px,py),1,c,tc,MLfont,stringFormat.format(dataset[-1][1]))
            # else:
                # draw_tag(surface,(px,py),0,c,tc,MLfont,stringFormat.format(dataset[-1][1]))
        
        pygame.draw.rect(WindowSurface,(0,0,0),(35,235,820,165)) # Blank load
        WindowSurface.blit(forceFont.render("{0:>9}".format(int(Load[0])),1,(255,0,0)),(10,210)) #Load
        pygame.draw.rect(WindowSurface,(0,0,0),(1230,235,650,165)) #Blank Displacement. This line may need tweaking.
        WindowSurface.blit(forceFont.render("{0:>7.2f}\"".format(td),1,(255,0,0)),(1175,210)) #Displacement

        pygame.draw.lines(WindowSurface,(0,100,255),0,((1230, 1020), (1205, 995), (1205, 445), (1230, 420)),3) # Fix overwrite
        
        pygame.display.update()
    #f.close()
    pygame.quit()

timev = 0

tclass = IOThread() ## create instance
tclass.start() ## start class running


Main()






