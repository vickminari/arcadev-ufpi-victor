import pygame
import time
import random

screen_width = 1000
screen_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
gray = (128, 128, 128)
dark_gray = (64, 64, 64)
light_gray = (192, 192, 192)
orange = (255, 165, 0)
pink = (255, 192, 203)
purple = (128, 0, 128)

colors = [black, white, red, green, blue, yellow, cyan, magenta, gray, dark_gray, light_gray, orange, pink, purple]

pygame.init()
window = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont('Tohama',40, True,False)


running = True

# square = {
#     'x': 100,
#     'y': 100,
#     'size': 50,
#     'speed_x': 20,
#     'speed_y': 20,
#     'color': white
# }

dvd = {
    'x': 100,
    'y': 100,
    'size': 50,
    'speed_x': 20,
    'speed_y': 20,
    'color': white
}

while(running):
    pygame.draw.rect(window, black, pygame.Rect(0,0,screen_width, screen_height))
    # pygame.draw.rect(window,(0,255,0), pygame.Rect(10,10,100,100))
    # pygame.draw.rect(window,(0,0,255), pygame.Rect(100,100,200,100))
    # pygame.draw.circle(window,(100,30,100),((300,100),50))
    # pygame.draw.polygon(window,(0,200,200),((10,150),(100,200),(200,300),(240,100),(20,10)))
    # pygame.draw.ellipse(window,(250,0,0), pygame.Rect(100,100,200,100))
    window.blit(font.render('DVD', False, dvd['color']), (dvd['x'], dvd['y']))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # pygame.draw.rect(window, square['color'], pygame.Rect(square['x'], square['y'], square['size'], square['size']))
    
    if dvd['x'] + dvd['size'] >= screen_width or dvd['x'] <= 0:
        dvd['speed_x'] = dvd['speed_x']* -1
        dvd['color'] = random.choice(colors)
    if dvd['y'] + dvd['size']/2 >= screen_height or dvd['y'] <= 0:
        dvd['speed_y'] = dvd['speed_y']* -1
        dvd['color'] = random.choice(colors)
        
    dvd['x'] += dvd['speed_x']
    dvd['y'] += dvd['speed_y']

    
        

    pygame.display.update()
    time.sleep(0.16)
