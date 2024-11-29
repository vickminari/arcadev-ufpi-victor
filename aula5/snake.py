import random
import pygame
import time

screen_width = 600
screen_height = 400

preto = (0,0,0)
branco = (255,255,255)
vermelho = (255,0,0)

cores = [preto, branco, preto, branco, preto, vermelho]
cor = 1
def atualizar_cor(cor):
    cor += 1
    if cor >= len(cores):
        cor = 0
    return cor

def iniciar_jogo():
    head = Head(20,40)
    tail1 = Segment(head, 0)
    tail = Segment(tail1, cor)
    food = Food(random.randint(0,screen_width//20 - 1) * 20, random.randint(0,screen_height//20 - 1) * 20)
    return head, tail, food

#classes

class Head():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 20
        self.dir = "right"
        self.score = 0
    
    def setUp(self):
        if self.dir != "down":
            self.dir = "up"
    
    def setDown(self):
        if self.dir != "up":
            self.dir = "down"
        
    def setRight(self):
        if self.dir != "left":
            self.dir = "right"
    
    def setLeft(self):
        if self.dir != "right":
            self.dir = "left"
    
    def update(self):
        if self.dir == "right":
            self.x += self.size
        elif self.dir == "left":
            self.x -= self.size
        elif self.dir == "up":
            self.y -= self.size
        elif self.dir == "down":
            self.y += self.size
            
    def checkCollide(self, x, y, w, h):
        return pygame.Rect(self.x, self.y, self.size, self.size).colliderect(pygame.Rect(x,y,w,h))
        
    def render(self, window):
        pygame.draw.rect(window, preto, pygame.Rect(self.x, self.y, self.size, self.size))

class Segment():
    def __init__(self, pattern, cor):
        self.x = pattern.x
        self.y = pattern.y
        self.pattern = pattern
        self.size = 20
        self.color = cores[cor]
        
    def update(self):
        self.x = self.pattern.x
        self.y = self.pattern.y
        self.pattern.update()
        
    def render(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.size, self.size))
        self.pattern.render(window)
        
class Food():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 20
        
    def render(self,window):
        pygame.draw.rect(window, (0, 200, 0), pygame.Rect(self.x, self.y, self.size, self.size))
        
#inits 
         
pygame.init()
window = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont('Tohama',40, True,False)

running = True
pause = False
game_over = False

head, tail, food = iniciar_jogo()

# head = Head(20,40)
# tail1 = Segment(head, 0)
# tail = Segment(tail1, cor)
# food = Food(random.randint(0,screen_width//20 - 1) * 20, random.randint(0,screen_height//20 - 1) * 20)

while(running):
    pygame.draw.rect(window, (128,128,128), pygame.Rect(0,0,screen_width, screen_height))

    if game_over:
        pause = True
        game_over_text = font.render('Game Over. Press R to Restart', True, (0, 0, 0))
        window.blit(game_over_text, (screen_width//2 - 200, screen_height//2 - 20))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    head, tail, food = iniciar_jogo()
                    game_over = False
                    pause = False
                    break
        continue
    
    score_text = font.render(f'{head.score}', True, (0, 0, 0))
    window.blit(score_text, (10, 10))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w:
                head.setUp()
            if event.key == pygame.K_s:
                head.setDown()
            if event.key == pygame.K_d:
                head.setRight()
            if event.key == pygame.K_a:
                head.setLeft()
            if event.key == pygame.K_p:
                pause = not pause
    

    if not pause:
        tail.update()
    # if game_over:
    #     pause = True
    #     game_over_text = font.render('Game Over. Press R to Restart', True, (0, 0, 0))
    #     window.blit(game_over_text, (screen_width//2 - 100, screen_height//2 - 20))

    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_r:
    #                 head, tail, food = iniciar_jogo()
    #                 game_over = False
    #                 pause = False
    #                 break
        # if pygame.key.get_pressed()[pygame.K_r]:
        #     head = Head(20,40)
        #     tail1 = Segment(head, 0)
        #     tail = Segment(tail1, cor)
        #     food = Food(random.randint(0,screen_width//20 - 1) * 20, random.randint(0,screen_height//20 - 1) * 20)
        #     cor = 1
        #     game_over = False
    
    
    if(head.checkCollide(food.x, food.y, food.size, food.size)):
        new_tail = Segment(tail, cor)
        tail = new_tail
        head.score += 1
        cor = atualizar_cor(cor)
        food = Food(random.randint(0,screen_width//20 - 1) * 20, random.randint(0,screen_height//20 - 1) * 20) 
    
    if head.x < 0:
        head.x = screen_width
    if head.x > screen_width:
        head.x = 0
    if head.y < 0:
        head.y = screen_height
    if head.y > screen_height:
        head.y = 0

    current_segment = tail
    while isinstance(current_segment, Segment):
        if head.checkCollide(current_segment.x, current_segment.y, current_segment.size, current_segment.size):
            game_over = True
            break
        current_segment = current_segment.pattern
    


    tail.render(window)
    food.render(window)
    
    pygame.display.update()
    time.sleep(0.1)