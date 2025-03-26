from pygame.font import Font
import pygame
from pygame import Surface, Rect, font

from codigo.Const import WINDOW_WIDTH, WINDOW_HEIGHT, NEW_GAME, EXIT, SCORE
from codigo.Level import Level


class TelaInicial:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load(r'C:\Users\icaro\PycharmProjects\DarkMonster\asset\assets\PNG\2\imglevelfull.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, menu_option=0):
        pygame.mixer_music.load(r'C:\Users\icaro\PycharmProjects\DarkMonster\asset\assets\sommenu.wav')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text("Dark", (250, 250, 250), ((WINDOW_WIDTH / 2), 140), 50)
            self.menu_text("Monster", (250, 250, 250), ((WINDOW_WIDTH / 2), 180), 50)

            letter_spacing = -1

            total_width = sum(
                [self.text_width(NEW_GAME[i], 20) + letter_spacing for i in range(len(NEW_GAME))]) - letter_spacing
            offset = (WINDOW_WIDTH / 2) - (total_width / 2)

            for i in range(len(NEW_GAME)):
                text_color = (255,20,20) if menu_option == 0 else (181, 181, 181)
                self.menu_text(NEW_GAME[i], text_color, (offset, 290), 20)
                offset += self.text_width(NEW_GAME[i], 20) + letter_spacing

            total_width_score = sum(
                [self.text_width(SCORE[i], 20) + letter_spacing for i in range(len(SCORE))]
            ) - letter_spacing
            offset_score = (WINDOW_WIDTH / 2) - (total_width_score / 2)

            for i in range(len(SCORE)):
                text_color_score = (255,20,20) if menu_option == 1 else (181, 181, 181)
                self.menu_text(SCORE[i], text_color_score, (offset_score, 340), 20)
                offset_score += self.text_width(SCORE[i], 20) + letter_spacing

            total_width_exit = sum(
                [self.text_width(EXIT[i], 20) + letter_spacing for i in range(len(EXIT))]) - letter_spacing
            offset_exit = (WINDOW_WIDTH / 2) - (total_width_exit / 2)

            for i in range(len(EXIT)):
                text_color_exit = (255, 20, 20) if menu_option == 2 else (181, 181, 181)
                self.menu_text(EXIT[i], text_color_exit, (offset_exit, 390), 20)
                offset_exit += self.text_width(EXIT[i], 20) + letter_spacing

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option+1)%3
                    elif event.key == pygame.K_UP:
                        menu_option = (menu_option-1)%3
                    if event.key == pygame.K_RETURN:
                        if menu_option == 0:
                            print("PLAY")
                            level = Level(self.window,"LEVEL", NEW_GAME)
                            level.run()
                        elif menu_option == 1:
                            print("RANK")
                        elif menu_option == 2:
                            pygame.quit()
                            quit()

            pygame.display.flip()

    def menu_text(self, text: str, text_color: tuple, text_center_pos: tuple, text_size: int):
        text_font: Font = pygame.font.SysFont(name="Courier ", size=text_size, bold=True)
        outline_color = (3, 3, 3)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        for x, y in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            self.window.blit(text_font.render(text, True, outline_color), text_rect.move(x, y))

        self.window.blit(source=text_surf, dest=text_rect)

    def text_width(self, text, size):
        font = pygame.font.SysFont("Courier", size, bold=True)
        return font.size(text)[0] + 7
