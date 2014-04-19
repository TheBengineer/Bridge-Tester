image_to_move = "horn.jpg"

import pygame
from pygame.locals import *

pygame.mixer.pre_init(44100, -16 , 2 , 2048)
pygame.init()
pygame.display.set_caption("Drive the car")
screen = pygame.display.set_mode((800, 800), 0, 32)
background = pygame.image.load(image_to_move).convert()

pygame.init()

sound = pygame.mixer.music.load("aoogah.mp3")

x, y = 0, 0
move_x, move_y = 0, 0


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            break

        #Changes the moving variables only when the key is being pressed
        if event.type == KEYDOWN:
            pygame.mixer.music.play()
            if event.key == K_LEFT:
                move_x = -2
            if event.key == K_RIGHT:
                move_x = 2
            if event.key == K_DOWN:
                move_y = 2
            if event.key == K_UP:
                move_y = -2


        #Stops moving the image once the key isn't being pressed
        elif event.type == KEYUP:
            pygame.mixer.music.stop()
            if event.key == K_LEFT:
                move_x = 0
            if event.key == K_RIGHT:
                move_x = 0
            if event.key == K_DOWN:
                move_y = 0
            if event.key == K_UP:
                move_y = 0

    x+= move_x
    y+= move_y

    screen.fill((255, 255, 255))
    screen.blit(background, (x, y))

    pygame.display.update()
