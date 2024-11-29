import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake segment class
class Segment:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None

# Snake class
class Snake:
    def __init__(self):
        self.head = Segment(WIDTH // 2, HEIGHT // 2)
        self.tail = self.head
        self.direction = RIGHT
        self.grow = False

    def move(self):
        new_head = Segment(self.head.x + self.direction[0] * CELL_SIZE, self.head.y + self.direction[1] * CELL_SIZE)
        new_head.next = self.head
        self.head = new_head

        if not self.grow:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
        else:
            self.grow = False

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def check_collision(self):
        # Check wall collision
        if self.head.x < 0 or self.head.x >= WIDTH or self.head.y < 0 or self.head.y >= HEIGHT:
            return True
        # Check self collision
        current = self.head.next
        while current:
            if self.head.x == current.x and self.head.y == current.y:
                return True
            current = current.next
        return False

    def grow_snake(self):
        self.grow = True

    def draw(self, screen):
        current = self.head
        while current:
            pygame.draw.rect(screen, GREEN, (current.x, current.y, CELL_SIZE, CELL_SIZE))
            current = current.next

# Food class
class Food:
    def __init__(self):
        self.x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        self.y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, CELL_SIZE, CELL_SIZE))

    def relocate(self):
        self.x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        self.y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE

# Main game loop
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)

        snake.move()

        if snake.head.x == food.x and snake.head.y == food.y:
            snake.grow_snake()
            food.relocate()

        if snake.check_collision():
            running = False

        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.flip()
        clock.tick(5)

    pygame.quit()

if __name__ == "__main__":
    main()