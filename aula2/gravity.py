import pygame
import time
import math

screen_width = 600
screen_height = 400

black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()
window = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont('Tohama',40, True,False)

running = True

quadrado = {
    "x": 100,
    "y": 100,
    "size": 100,
    "speed_x": 10,
    "speed_y": 10
}

gravity = 1

left = False
right = False
up = False
down = False
can_jump = True

while(running):
    pygame.draw.rect(window, white, pygame.Rect(0,0,screen_width, screen_height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            left = True
        if event.key == pygame.K_RIGHT:
            right = True
        if event.key == pygame.K_UP:
            up = True
        # if event.key == pygame.K_DOWN:
        #     down = True
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            left = False
        if event.key == pygame.K_RIGHT:
            right = False
        if event.key == pygame.K_UP:
            up = False
        # if event.key == pygame.K_DOWN:
        #     down = False
    
    if(left):
        quadrado["speed_x"] = -5
    elif(right):
        quadrado["speed_x"] = 5
    else:
        quadrado["speed_x"] = 0
    
    if(up and quadrado["y"] + quadrado["size"] >= screen_height):
        quadrado["speed_y"] = -20
    # elif(down and quadrado["y"] + quadrado["size"] < screen_height):
    #     quadrado["speed_y"] = 5

    # if(up):
    #     quadrado["y"] -= quadrado["speed_y"]
    # elif(down):
    #     quadrado["y"] += quadrado["speed_y"]
    
    quadrado["x"] += quadrado["speed_x"]
    quadrado["y"] += quadrado["speed_y"]
    # if quadrado["y"] + quadrado["size"] < screen_height:
    #     quadrado["speed_y"] += gravity
    # else:
    #     can_jump = True
    #     quadrado["speed_y"] = screen_height - quadrado["size"]
    if quadrado["y"] + quadrado["size"] >= screen_height:
        quadrado["speed_y"] = 0
    else:
        quadrado["speed_y"] += gravity
    if quadrado["x"] + quadrado["size"] >= screen_width or quadrado["x"] <= 0:
        quadrado["speed_x"] = 0

            
        # if event.type == pygame.MOUSEBUTTONUP:
        #     print(event)
    
    # print(pygame.mouse.get_pressed())      

    pygame.draw.rect(window,(0,0,0), pygame.Rect(quadrado["x"],quadrado["y"],quadrado["size"],quadrado["size"]))
    
    pygame.display.update()
    time.sleep(0.01)
    
pygame.quit()