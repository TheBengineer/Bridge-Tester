import pygame, random, sys, math,time,commands,os
from pygame.locals import *
#import cProfile
import Reactor as rec
#import Brence as br
#import Decay



def Main():
    ################ Pygame Init
    pygame.init()
    fpsclock = pygame.time.Clock()
    WindowSurface = pygame.display.set_mode((640,480))
    pygame.display.set_caption("ADC Test")
 
    ####################    Pygame Declarations
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

        lines.insert(0,int(random.random()*100))
        lines = lines[:400]
        tm = time.time()*50
        rec.Draw_Chart(WindowSurface,10,10,500,400,lines,(0,100,0,100),(255,100,0),(255,255,255),3)
  
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
        pygame.display.update()
        fpsclock.tick(50)
    pygame.quit()
    #raw_input("Pres Enter to exit...")

Main()
#cProfile.run("Main()")
