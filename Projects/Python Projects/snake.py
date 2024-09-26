import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 400
HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Snake initial position
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_dir = (0, 1)

# Food initial position
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Score
score = 0
font = pygame.font.Font(None, 36)

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0]*GRID_SIZE, segment[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, (food[0]*GRID_SIZE, food[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))

def move_snake():
    global snake, food, score
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)
    
    if new_head == food:
        score += 1
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

def check_collision():
    if (snake[0][0] < 0 or snake[0][0] >= GRID_WIDTH or
        snake[0][1] < 0 or snake[0][1] >= GRID_HEIGHT or
        snake[0] in snake[1:]):
        return True
    return False

# Main game loop
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, 1):
                snake_dir = (0, -1)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -1):
                snake_dir = (0, 1)
            elif event.key == pygame.K_LEFT and snake_dir != (1, 0):
                snake_dir = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-1, 0):
                snake_dir = (1, 0)
    
    move_snake()
    if check_collision():
        game_over = True
    
    screen.fill((0, 0, 0))
    draw_grid()
    draw_snake()
    draw_food()
    
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(10)

pygame.quit()