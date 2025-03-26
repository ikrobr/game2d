from math import trunc

import pygame.display

from codigo import Personagem
from codigo.FactoryPerson import FactoryPerson


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.personagem_list: list[Personagem] = []
        self.personagem_list.extend(FactoryPerson.get_personagem('floresta'))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for pers in self.personagem_list:
                self.window.blit(source=pers.surf, dest=pers.rect)
                pers.move()
            pygame.display.flip()
        pass