import pygame
from game.assets import alien_bullet_img, explosion2_fx
from game.game_objects.explosion import Explosion
from settings import explosion_group, SCREEN_HEIGHT, spaceship_group
from game.game_objects.spaceship import spaceship

class Alien_Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = alien_bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
    
    def update(self):
        self.rect.y += 2
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
        if pygame.sprite.spritecollide(self, spaceship_group, False, pygame.sprite.collide_mask):
            self.kill()
            explosion2_fx.play()
            spaceship.health_remaining -= 1
            explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
            explosion_group.add(explosion)
            
