from abc import ABC, abstractmethod

import pygame.image

#fazer importações das funcionalidades


class Personagem(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load(r'C:\Users\icaro\PycharmProjects\DarkMonster\asset\assets\PNG\2'+name+'.png').convert_alpha()

        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.velocidade = 0
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        pass