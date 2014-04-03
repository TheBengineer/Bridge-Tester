l = [0]*10
l += [1]
l += [1]
l += [1]
l += [1]
l += [1]
l += [1]
print l
 



import pygame, random, sys, math,time,commands,os
from pygame.locals import *
import cProfile
import Reactor as rec
import Brence as br
import Decay
import smbus






def Main():
    ################ Pygame Init
    pygame.init()
    fpsclock = pygame.time.Clock()
    WindowSurface = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Pygame Test ")
    d = Decay.Decay()
    bus = smbus.SMBus(1)
    ADC = os.system("i2cset -y 1 0x48 0x01 0x80E0 w")

    ####################    Pygame Declarations
    testSurface = pygame.image.load("test.png")
    MouseSurface = pygame.Surface((32, 32), 0, 8).convert_alpha()
    MouseSurface.fill((0,100,0,0))
    #MouseSurface.convert_alpha()
    pygame.draw.line(MouseSurface,(0,255,0),(16,0),(16,32),1)
    pygame.draw.line(MouseSurface,(0,255,0),(0,16),(32,16),1)

    ############################# Classes
 
        
    
    #################### Declarations
 
    lines = [0.0]*400
    red = pygame.Color(255,0,0)
    green = pygame.Color(0,255,0)
    blue = pygame.Color(0,0,255)
    white = pygame.Color(255,255,255)
    black = pygame.Color(0,0,0)
    mousex, mousey = 0,0
    font = pygame.font.Font("freesansbold.ttf",12)
    run = 1
    
    ######################## Non-Reactor specific functions
    def keyPressed(inputKey):
        keysPressed = pygame.key.get_pressed()
        if keysPressed[inputKey]:
            return True
        else:
            return False
    
    ######################## Main Loop
    while run:
        ############## Window
        WindowSurface.fill(black) # Screen Redraw
        #pygame.draw.polygon(WindowSurface,red,((100,0),(100,200),(150,175)))
        #PixArr = pygame.PixelArray(WindowSurface)
        #for x in range(100,600,10):
        #    for y in range(100,400,10):
        #        WindowSurface.blit(testSurface,(x,y))
                #PixArr[x][y] = pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        #del PixArr
        
        ###################Reactor update

        ADC = commands.getoutput("i2cget -y 1 0x48 0x00 w")
        #print "ADC: ",ADC
        try:
            ADCNormalized = int(ADC,16)/655.35#327.675
        except:
            print "I2c Error"
            ADCNormalized = 0
        #print ADCNormalized
        lines.insert(0,ADCNormalized)
        lines = lines[:400]
        tm = time.time()*50
        rec.Draw_Chart(WindowSurface,10,10,400,200,lines,(0,100,0,100),(255,100,0),(255,255,255),3)
  
        ############################# Event dling
        for event in pygame.event.get():
            if event.type == QUIT:
                run = 0
                break
            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = 0
                    break
        ######################### Pygame drawing
        WindowSurface.blit(MouseSurface,(mousex-16,mousey-16))
        WindowSurface.blit(font.render(str((mousex,mousey)),1,(100,100,100)),(mousex+10,mousey))
        WindowSurface.blit(font.render("ADC: "+str(ADC)+" "+str(ADCNormalized),1,(100,255,100)),(10,40))
        pygame.display.update()
        fpsclock.tick(50)
    pygame.quit()
    #raw_input("Pres Enter to exit...")

Main()
#cProfile.run("Main()")
