from settings import screen, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, clock
from game.assets import background_img, terra_img, lua_img

def draw_background_img():
    screen.blit(background_img, (0, 0))
    screen.blit(terra_img, (100, 350))
    screen.blit(lua_img, (500, 100))

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))