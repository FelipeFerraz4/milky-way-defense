import pygame
from pygame import mixer
from pygame.locals import *
from settings import *
from game.assets import *
from game.story import *
from game.background import *
from game.game_objects.spaceship import spaceship 
from game.game_objects.alien import create_aliens
from game.game_objects.alien_bullets import Alien_Bullets
import random

run = True
show_story()
while run:
    clock.tick(FPS)
    
    draw_background_img()
    if countdown == 0:
        draw_text(f'NAVES INIMIGAS RESTANTES: {score}', fonte1, WHITE, 10, 0)
        draw_text('FASE 1', fonte1, WHITE, (SCREEN_WIDTH//2 + 150), 0)
        if len(alien_group) < quantity_alien:
            score -= (quantity_alien - len(alien_group))
            quantity_alien = len(alien_group)
        
        time_now = pygame.time.get_ticks()
        if time_now - last_alien_shot > ALIEN_COOLDOWN and len(alien_bullet_group) < 5 and len(alien_group) > 0:
            attacking_alien = random.choice(alien_group.sprites())
            alien_bullet = Alien_Bullets(attacking_alien.rect.centerx, attacking_alien.rect.bottom)
            alien_bullet_group.add(alien_bullet)
            last_alien_shot = time_now
    
        if len(alien_group) <= 0:
            game_over = 1 
               
        if game_over == 0:
            game_over = spaceship.update()
            bullet_group.update()
            alien_group.update()
            alien_bullet_group.update()
        else:
            if game_over == -1:
                draw_text('A RAÇA HUMANA FOI DESTRUIDA!', fonte1, WHITE, (SCREEN_WIDTH//2 - 235), (SCREEN_HEIGHT//2 + 80))
            elif game_over == 1:
                draw_text('A TERRA ESTÁ SALVA!', fonte1, WHITE, (SCREEN_WIDTH//2 - 170), (SCREEN_HEIGHT//2 + 80))
                
        
    if countdown > 0:
        draw_text('PREPARE-SE COMANDANTE!', fonte1, WHITE, (SCREEN_WIDTH//2 - 205), (SCREEN_HEIGHT//2 + 100))
        draw_text(f'DECOLAGEM EM {countdown}', fonte2, WHITE, (SCREEN_WIDTH//2 - 95), (SCREEN_HEIGHT//2 + 140))
        count_timer = pygame.time.get_ticks()
        if count_timer - last_count > 1000:
            countdown -= 1
            last_count = count_timer
    
    explosion_group.update()
    
    spaceship_group.draw(screen)
    bullet_group.draw(screen)
    alien_group.draw(screen)
    alien_bullet_group.draw(screen)
    explosion_group.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
            
pygame.quit()
exit()
