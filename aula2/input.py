import pygame
import time
import random

screen_width = 1000
screen_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()
window = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont('Tohama',40, True,False)

running = True

while(running):
    pygame.draw.rect(window, black, pygame.Rect(0,0,screen_width, screen_height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if event.type == pygame.KEYDOWN:
        # if event.key == pygame.K_UP:
        #     print('Up')
        # if event.key == pygame.K_DOWN:
        #     print('Down')
        if event.key == pygame.K_LEFT:
            print('Left')
        if event.key == pygame.K_RIGHT:
            print('Right')
    
    if event.type == pygame.MOUSEBUTTONUP:
        print(event)


    
        

    pygame.display.update()
    time.sleep(0.16)