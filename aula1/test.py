import pygame
import sys

# Inicializar o pygame
pygame.init()

# Dimensões da janela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Colisão com a borda da janela")

# Cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Parâmetros do objeto (bola)
ball_radius = 20
ball_x = width // 2
ball_y = height // 2
ball_speed_x = 5
ball_speed_y = 5

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualizar a posição da bola
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Verificar colisão com as bordas
    if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
        ball_speed_x = -ball_speed_x  # Inverte a direção horizontal
    if ball_y - ball_radius < 0 or ball_y + ball_radius > height:
        ball_speed_y = -ball_speed_y  # Inverte a direção vertical

    # Desenhar o fundo e a bola
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_radius)
    pygame.display.flip()

    # Controlar a taxa de atualização
    pygame.time.Clock().tick(60)
