import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Paddle
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
BALL_SIZE = 20
ball = pygame.Rect(random.randint(0, WIDTH - BALL_SIZE), 0, BALL_SIZE, BALL_SIZE)
ball_speed = 5

# Game variables
score = 0
font = pygame.font.Font(None, 36)

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddle with mouse
    paddle.x = pygame.mouse.get_pos()[0] - PADDLE_WIDTH // 2
    paddle.x = max(0, min(paddle.x, WIDTH - PADDLE_WIDTH))

    # Move the ball
    ball.y += ball_speed

    # Check for collision with paddle
    if ball.colliderect(paddle):
        score += 1
        ball.y = 0
        ball.x = random.randint(0, WIDTH - BALL_SIZE)
        ball_speed += 0.5

    # Check if ball is out of bounds
    if ball.y > HEIGHT:
        ball.y = 0
        ball.x = random.randint(0, WIDTH - BALL_SIZE)

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddle
    pygame.draw.rect(screen, BLUE, paddle)

    # Draw ball
    pygame.draw.ellipse(screen, RED, ball)

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()