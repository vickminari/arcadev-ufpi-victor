import pygame
import time

screen_width = 600
screen_height = 400

pygame.init()
window = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont('Tohama',40, True,False)

running = True

while(running):
    pygame.draw.rect(window, (0,0,0), pygame.Rect(0,0,screen_width, screen_height))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    time.sleep(0.16)
