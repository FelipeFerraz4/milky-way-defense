import pygame
from settings import screen, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, clock

def show_story():
    story_text = [
        "MILKY WAY DEFENSE",
        "",
        "Na data estelar 2525",
        "A Via Láctea está sob ataque.",
        "",
        "Forças inimigas desconhecidas estão avançando rumo à Terra,",
        "destruindo colônias humanas por todo o sistema galáctico.",
        "",
        "Você é um piloto espacial da frota de defesa terrestre,",
        "designado para proteger o planeta e deter a onda de invasores.",
        "",
        "Esta é apenas a Fase 1.",
        "",
        "A sua missão será proteger a órbita da Terra, enfrentando",
        "e destruindo todas as ameaças.",
        "",
        "O destino da humanidade... e da Via Láctea... está em suas mãos.",
        "",
        "Prepare-se para a batalha!"
    ]

    scroll_y = SCREEN_HEIGHT  # Começa fora da tela
    speed = 0.8  # Velocidade de rolagem
    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background.fill((0, 0, 0))  # Fundo preto

    story_font = pygame.font.SysFont("arial", 20)  # Fonte comum

    while True:
        screen.blit(background, (0, 0))

        for i, line in enumerate(story_text):
            text_surface = story_font.render(line, True, (255, 255, 0))  # Cor amarela
            text_rect = text_surface.get_rect(midtop=(SCREEN_WIDTH // 2, scroll_y + i * 30))
            screen.blit(text_surface, text_rect)

        scroll_y -= speed

        # Verifica se a última linha já saiu completamente da tela
        last_line_y = scroll_y + len(story_text) * 30
        if last_line_y < 0:
            return  # Inicia a próxima fase automaticamente

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                return  # Opcional: tecla ainda pode pular a intro

        pygame.display.update()
        clock.tick(FPS)
