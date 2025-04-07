import pygame
from settings import *
from game.assets import *
from game.game_objects.explosion import Explosion
from game.game_objects.bullets import Bullets

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.last_shot = pygame.time.get_ticks()
        self.health_start = health
        self.health_remaining = health
        
    
    def update(self):
        speed = 5
        cooldown = 500
        game_over = 0
        
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 5:
            self.rect.x -= speed
        if key[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH - 5:
            self.rect.x += speed
        
        time_now = pygame.time.get_ticks()    
        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            laser_fx.play()
            bullet = Bullets(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            self.last_shot = time_now
        
        self.mask = pygame.mask.from_surface(self.image)
            
        pygame.draw.rect(screen, RED, (self.rect.x, (self.rect.bottom + 2), self.rect.width, 10))
        if self.health_remaining > 0:
            pygame.draw.rect(screen, GREEN, (self.rect.x, (self.rect.bottom + 2), 
                                             int(self.rect.width * ((self.health_remaining - 1)/(self.health_start-1))), 10))
        elif self.health_remaining <= 0:
            explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
            explosion_group.add(explosion)
            self.kill()
            game_over = -1
            return game_over
        return game_over
        
spaceship = Spaceship((SCREEN_WIDTH//2), SCREEN_HEIGHT - 40, 3)
spaceship_group.add(spaceship)