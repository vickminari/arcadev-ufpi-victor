import pygame
import time
import math
import random


screen_width = 600
screen_height = 400

pygame.init()
window = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont('Tohama',40, True,False)

#classes

class Player():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.w = 20
        self.h = 100
        self.speed = 5
        
        self.up = False
        self.down = False
    
    def setUp(self,mode):
        self.up = mode
    
    def setDown(self,mode):
        self.down = mode
    
    def update(self):
        if(self.up and self.y > 0):
            self.y -= self.speed
        elif(self.down and self.y < screen_height-self.h):
            self.y += self.speed
    
    def render(self,window):
        pygame.draw.rect(window, (255,255,255), pygame.Rect(self.x,self.y,self.w,self.h))

class Ball():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.r = 20
        self.dx = 5
        self.dy = 5
    
    def update(self, player_1, player_2):
        if(self.y < 0 or self.y + self.r > screen_height):
            self.dy *= -1
        if(self.x < 0 or self.x > screen_width):
            self.x = screen_width/2
            self.y = screen_height/2
            self.dx *= random.choice([-1, 1])
            self.dy *= random.choice([-1, 1])
        if(self.x < player_1.x + player_1.w and self.y > player_1.y and self.y < player_1.y + player_1.h):
            self.dx *= -1
        if(self.x + self.r > player_2.x and self.y > player_2.y and self.y < player_2.y + player_2.h):
            self.dx *= -1
        
        self.x += self.dx
        self.y += self.dy
    
    def render(self,window):
        pygame.draw.ellipse(window, (255,255,255), pygame.Rect(self.x,self.y,self.r,self.r))

#variables
player_1 = Player(10,120)
player_2 = Player(screen_width-30,120)
ball = Ball(screen_width/2,screen_height/2)

running = True

while(running):
    pygame.draw.rect(window, (0,0,0), pygame.Rect(0,0,screen_width, screen_height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                player_2.setUp(True)
            if event.key == pygame.K_DOWN:
                player_2.setDown(True)
            if event.key == pygame.K_w:
                player_1.setUp(True)
            if event.key == pygame.K_s:
                player_1.setDown(True)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_2.setUp(False)
            if event.key == pygame.K_DOWN:
                player_2.setDown(False)
            if event.key == pygame.K_w:
                player_1.setUp(False)
            if event.key == pygame.K_s:
                player_1.setDown(False)
        

    player_1.update()
    player_2.update()
    ball.update(player_1, player_2)
    player_1.render(window)
    player_2.render(window)
    ball.render(window)
    
    pygame.display.update()
    time.sleep(0.05)