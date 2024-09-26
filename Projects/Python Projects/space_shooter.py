import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player
player_width = 50
player_height = 50
player = pygame.Rect(WIDTH//2 - player_width//2, HEIGHT - player_height - 10, player_width, player_height)
player_speed = 5

# Bullets
bullet_width = 5
bullet_height = 10
bullets = []
bullet_speed = 7

# Enemies
enemy_width = 50
enemy_height = 50
enemies = []
enemy_speed = 2

# Score
score = 0
font = pygame.font.Font(None, 36)

def draw_player():
    pygame.draw.rect(screen, WHITE, player)

def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

def move_bullets():
    for bullet in bullets:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

def move_enemies():
    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
            global score
            score -= 1

def check_collisions():
    global score
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player.centerx - bullet_width//2, player.top, bullet_width, bullet_height)
                bullets.append(bullet)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Spawn enemies
    if random.randint(1, 60) == 1:
        enemy = pygame.Rect(random.randint(0, WIDTH - enemy_width), 0, enemy_width, enemy_height)
        enemies.append(enemy)

    move_bullets()
    move_enemies()
    check_collisions()

    screen.fill(BLACK)
    draw_player()
    draw_bullets()
    draw_enemies()

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()