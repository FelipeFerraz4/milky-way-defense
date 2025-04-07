import pygame
from pygame import mixer

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

# Sons
explosion_fx = mixer.Sound("./assets/audio/explosion.wav")
explosion_fx.set_volume(0.25)

explosion2_fx = mixer.Sound("assets/audio/explosion2.wav")
explosion2_fx.set_volume(0.25)

laser_fx = mixer.Sound("assets/audio/laser.wav")
laser_fx.set_volume(0.25)

# Fontes
fonte1 = pygame.font.Font("./assets/fonte/Pixeled.ttf", 20)
fonte2 = pygame.font.Font("./assets/fonte/Pixeled.ttf", 15)
fonte3 = pygame.font.Font("./assets/fonte/Pixeled.ttf", 30)

# Imagens
background_img = pygame.image.load("./assets/image/bg.png")
terra_img = pygame.image.load("./assets/image/terra.png")
lua_img = pygame.image.load("./assets/image/lua.png")
player_img = pygame.image.load("./assets/image/player.png")
bullet_img = pygame.image.load("./assets/image/bullet.png")
alien_bullet_img = pygame.image.load("./assets/image/alien_bullet.png")
explosion_imgs = [pygame.image.load(f"./assets/image/exp{i}.png") for i in range(1, 6)]
