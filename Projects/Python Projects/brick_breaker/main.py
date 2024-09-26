import pygame
import random

# Init Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Brick Breaker")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Clock
clock = pygame.time.Clock()

# Paddle & Ball
# Paddle
paddle_width, paddle_height = 100, 10
paddle = pygame.Rect(width // 2 - paddle_width // 2, height - 30, paddle_width, paddle_height)

# Ball
ball_radius = 10
ball = pygame.Rect(width // 2, height // 2, ball_radius * 2, ball_radius * 2)
ball_speed = [4 , -4]

# Bricks
brick_width, brick_height = 60, 20
bricks = []


def create_bricks(rows, cols):
    for row in range(rows):
        for col in range(cols):
            brick = pygame.Rect(col * (brick_width + 10) + 35, row * (brick_height + 10) + 50, brick_width, brick_height)
            bricks.append(brick)
            

create_bricks(5, 10)

# Bricks speed
brick_speed = 1

def move_bricks():
    global brick_speed
    for brick in bricks:
        brick.y += brick_speed
    if bricks and bricks[0].y > height:
        bricks.pop(0)
        create_bricks(1, 10)
        brick_speed += 0.1
        
# Collisions
def handle_collisions():
    global ball_speed
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]
    for brick in bricks:
        if ball.colliderect(brick):
            ball_speed[1] = -ball_speed[1]
            bricks.remove(brick)
            break
        
# Power-Ups
power_ups = []


def create_pwr_up():
    pwr_up = pygame.Rect(random.randint(0, width - 20), 0, 20, 20)
    power_ups.append(pwr_up)
    
    
def move_pwr_ups():
    for pwr_up in power_ups:
        pwr_up.y +=2
        if pwr_up.colliderect(paddle):
            power_ups.remove(pwr_up)
            # Example power up: Increase paddle width
            paddle.width += 20
            break
        
        
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= 5
    if keys[pygame.K_RIGHT] and paddle.right < width:
        paddle.x += 5
        
        
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]
    
    if ball.left <= 0 or ball.right >= width:
        ball_speed[0] = - ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = - ball_speed[1]
    if ball.bottom >= height:
        running = False     # Game Over
        
        
    handle_collisions()
    move_bricks()
    move_pwr_ups()
    
    
    screen.fill(black)
    pygame.draw.rect(screen, white, paddle)
    pygame.draw.ellipse(screen, blue, ball)
    for brick in bricks:
        pygame.draw.rect(screen, red, brick)
    for pwr_up in power_ups:
        pygame.draw.rect(screen, white, pwr_up)
        
    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()