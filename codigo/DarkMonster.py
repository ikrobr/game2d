from codigo.TelaInicial import TelaInicial
from codigo.Const import WINDOW_WIDTH, WINDOW_HEIGHT

import pygame


class DarkMonster:
    def __init__(self):
        pygame.init()  # iniciando pygame
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT)) # pxs da janela

    def run(self):
        global TelaInicial
        while True:
            telaInicial = TelaInicial(self.window)
            telaInicial.run()
            pass

