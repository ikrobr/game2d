from codigo.Level import Level
from codigo.TelaInicial import TelaInicial
from codigo.Const import WINDOW_WIDTH, WINDOW_HEIGHT, NEW_GAME, SCORE

import pygame


class DarkMonster:
    def __init__(self):
        pygame.init()  # iniciando pygame
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT)) # pxs da janela

    def run(self):
        global TelaInicial
        while True:
            telaInicial = TelaInicial(self.window)
            menu_return = telaInicial.run()

            if menu_return == NEW_GAME:
                level = Level(self.window, 'Level', menu_return)
                level_return = level.run()
            elif menu_return == SCORE:
                pass
            else:
                pass

