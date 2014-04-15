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
        self.pressureAddress = 0x49 # Address of Pressure ADC
        self.distanceAddress = 0x48 # Address of Distance ADC (adddr hooked to vcc)
        self.ledAddresses = [0x60,0x61,0x62,0x63,0x64] # Addresses of LED 7 segment display Drivers
        self.bus = fakeIIC() # just init this in case something ties to use it.
        self.segmentLookup = [63, 6, 91, 79, 102, 109, 125, 7, 127, 111, 119, 124, 57, 94, 121, 113, 123]
        self.pressureArray = []
	self.lastPressure = 0
	self.lastDistance = 0
        self.Display = [0]*5
        if pi == 1: # running on a Pi?
            self.bus = self.initI2C(self.pressureAddress,self.distanceAddress)
    def initI2C(self,pressureA,distanceA):
        bus = smbus.SMBus(1)# Setup IIC
        bus.write_word_data(pressureA,0x01,0x80E0) # Default setup for Pressure
        bus.write_word_data(distanceA,0x01,0x80E0) # Default setup for Distance
        #LEDS don't need setup
        return bus
    def pollpress(self):
        readingraw = convertReading(self.bus.read_word_data(self.pressureAddress,0x00))
        pressure = readingraw/566.35
        if pressure < 90: 
                self.pressureArray.append([pressure,self.lastDistance,time.time()])#time.time is far away from reading, but should be ok
                return pressure
        else:
                return 0.0
    def setled(self,cellAddress,numberToDisplay):
        self.bus.write_byte_data(cellAddress, 0x44, self.segmentLookup[numberToDisplay])
    def getdist(self):
        readingraw = convertReading(self.bus.read_word_data(self.distanceAddress,0x00))
        distance = readingraw/566.35
        return distance
    def run(self):  ## dont need it here
        self.error = 0
        while self.error == 0:  ## Main thread program using passed variable
            self.lastPressure = self.pollpress()
            self.lastDistance = self.getdist()
            #print("Pressure",self.pressure)
            time.sleep(.005)
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
    xscale2 = (hsize+1)/DataHeightX
    yscale = (vsize+1)/DataHeightY
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
            lines.append(((i[0]*xscale2)+x-(DXMin*xscale2),y-(DYMin*yscale)+(i[1]*yscale)))
    pygame.draw.lines(surface,color,0,lines,stroke)
    pygame.draw.circle(surface,(255,0,0,128),(int(lines[-1][0]),int(lines[-1][1])),10)
    
    



def Main():
    ################ Pygame Init
    pygame.init()
    fpsclock = pygame.time.Clock()
    WindowSurface = pygame.display.set_mode((1000,500))
    pygame.display.set_caption("Pygame Test")
    
    
    ################# Pygame declarations
    #CustomImage = pygame.image.load("test.png")
    MouseSurface = pygame.Surface((32, 32), 0, 8).convert_alpha()
    MouseSurface.fill((0,100,0,0))
    pygame.draw.line(MouseSurface,(0,255,0),(16,0),(16,32),1)
    pygame.draw.line(MouseSurface,(0,255,0),(0,16),(32,16),1)
    
    font = pygame.font.Font("freesansbold.ttf",12)
    runProgram = 1
    mousex, mousey = 0,0
    lines = [0.0,0.0]*2
    Load = [0,110]
    Dist = [0,110]
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
        readings = 0
	pressures = 0
	distances = 0
        while len(tclass.pressureArray) > 1:
		tmpAr = tclass.pressureArray.pop()
		readings += 1
		pressures += tmpAr[0]
		distances += tmpAr[1]
        if readings > 0:
		tp = pressures/readings
		td = distances/readings
		if tp > Load[0]:
			Load[0] = tp
		if tp < Load[1]:
			Load[1] = tp
		if td > Dist[0]:
			Dist[0] = td
		if td < Dist[1]:
			Dist[1] = td
        	print Dist, Load
        	lines.append([td,tp])
        Draw_Chart(WindowSurface,10,10,800,400,lines,(0,len(lines)),(Dist[1],Dist[0]+1),(Load[1],Load[0]+1),(255,100,0),1,(255,255,255),3)
        
        #Draw
        WindowSurface.blit(MouseSurface,(mousex-16,mousey-16))
        pygame.display.update()
        fpsclock.tick(10)
    pygame.quit()



tclass = IOThread() ## create instance
tclass.start() ## start class running



Main()






