import pygame, time
pygame.mixer.init()
pygame.mixer.music.load("aoogah.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    time.sleep(4)
    pygame.mixer.music.play()
