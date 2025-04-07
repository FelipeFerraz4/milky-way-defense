import pygame
import random
from settings import alien_group

def create_aliens():
    from settings import ROWS, COLS
    for row in range(ROWS):
        for item in range(COLS):
            alien = Aliens(200 + item * 100, 90 + row * 70)
            alien_group.add(alien)

class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/image/alien" +
                                       str(random.randint(1, 4)) + ".png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_counter = 0
        self.move_direction = 1
        
        
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 125:
            self.move_direction *= -1
            self.move_counter *= self.move_direction

create_aliens()