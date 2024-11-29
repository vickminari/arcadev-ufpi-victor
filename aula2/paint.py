import pygame
import time
import math
import random

screen_width = 1080
screen_height = 720

pygame.init()
window = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont('Tohama',40, True,False)

running = True

balls = []

color = (0,0,0)

# black = (0, 0, 0)
# white = (255, 255, 255)
# red = (255, 0, 0)
# green = (0, 255, 0)
# blue = (0, 0, 255)
# yellow = (255, 255, 0)
# cyan = (0, 255, 255)
# magenta = (255, 0, 255)
# gray = (128, 128, 128)
# dark_gray = (64, 64, 64)
# light_gray = (192, 192, 192)
# orange = (255, 165, 0)
# pink = (255, 192, 203)
# purple = (128, 0, 128)

# colors = [black, white, red, green, blue, yellow, cyan, magenta, gray, dark_gray, light_gray, orange, pink, purple]

def random_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

while(running):
    pygame.draw.rect(window, (255,255,255), pygame.Rect(0,0,screen_width, screen_height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            color = random_color()
            balls.append({
                    "cor": color,
                    "x": x,
                    "y": y
                }
            )
        
        #original
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     x, y = event.pos
        #     balls.append({
        #             "cor": color,
        #             "x": x,
        #             "y": y
        #         }
        #     )
        
        # random color
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                r,g,b = random_color()
                color = (r,g,b)

        # original
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_a:
        #         color = (255,0,0)
        #     elif event.key == pygame.K_s:
        #         color = (0,255,0)
        #     elif event.key == pygame.K_d:
        #         color = (0,0,255)
        

    
    for ball in balls:
        ball["x"] += random.randint(-100,100)
        ball["y"] += random.randint(-100,100)
        pygame.draw.circle(window,ball["cor"],(ball["x"],ball["y"]),50)

    
    pygame.display.update()
    time.sleep(0.05)
    
pygame.quit()