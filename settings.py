import pygame
from pygame import mixer

# Display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)
pygame.display.set_caption('Milky Way Defense')


# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BG_COLOR = (0, 0, 20)

# Game settings
ROWS = 5
COLS = 5
ALIEN_COOLDOWN = 800
score = ROWS * COLS
quantity_alien = ROWS * COLS

last_alien_shot = pygame.time.get_ticks()
last_count = pygame.time.get_ticks()
clock = pygame.time.Clock()
countdown = 3
game_over = 0

spaceship_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
