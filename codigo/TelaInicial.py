from pygame.font import Font
import pygame
from pygame import Surface, Rect

from codigo.Const import WINDOW_WIDTH, WINDOW_HEIGHT, NEW_GAME


class TelaInicial:
    def __init__(self, window):
        self.window = window
        self.surf = (pygame.image.load
                     (r'C:\Users\icaro\PycharmProjects\DarkMonster\asset\assets\PNG\1\terrace.png'))
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        (pygame.mixer_music.load
         (r'C:\Users\icaro\PycharmProjects\DarkMonster\asset\assets\sommenu.wav'))
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text("Dark", (220, 220, 220), ((WINDOW_WIDTH / 2), 70), 50)
            self.menu_text("Monster", (220, 220, 220), ((WINDOW_WIDTH / 2), 120), 50)
            for i in range(len(NEW_GAME)):
                self.menu_text(NEW_GAME[i], (250, 250, 250), ((WINDOW_WIDTH / 2), 200 + 25 * i), 20)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text: str, text_color: tuple, text_center_pos: tuple, text_size: int):
        text_font: Font = pygame.font.SysFont(name="Courier New", size=text_size, bold=True)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
