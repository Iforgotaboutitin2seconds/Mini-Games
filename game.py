import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
PLAYER_COLOR = (0, 0, 255)
NORMAL_COLOR = (128, 128, 128)
ENEMY_COLOR = (255, 0, 0)
PLAYER_SPEED = 0.5
ORBIT_RADIUS = 100
ORBIT_SPEED = 0.02

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Dot:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)

# Create player dot
player = Dot(WIDTH // 2, HEIGHT // 2, PLAYER_COLOR)

# Create other dots
dots = []
for _ in range(20):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    color = NORMAL_COLOR if random.randint(0, 1) == 0 else ENEMY_COLOR
    dots.append(Dot(x, y, color))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and player.x > 0:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and player.x < WIDTH:
        player.x += PLAYER_SPEED
    if keys[pygame.K_UP] or keys[pygame.K_w] and player.y > 0:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s] and player.y < HEIGHT:
        player.y += PLAYER_SPEED

    # Update the positions of other dots
    for i, dot in enumerate(dots):
        angle = i * (2 * math.pi / len(dots))
        dot.x = player.x + int(ORBIT_RADIUS * math.cos(angle))
        dot.y = player.y + int(ORBIT_RADIUS * math.sin(angle))
        dot.color = NORMAL_COLOR

    # Collision detection
    for dot in dots:
        if abs(dot.x - player.x) < 20 and abs(dot.y - player.y) < 20:
            dot.color = PLAYER_COLOR

    # Draw everything
    screen.fill((0, 0, 0))
    player.draw(screen)
    for dot in dots:
        dot.draw(screen)

    pygame.display.flip()

pygame.quit()