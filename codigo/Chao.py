import pygame
from codigo.Personagem import Personagem
from codigo.Const import WINDOW_HEIGHT, WINDOW_WIDTH


class Chao(Personagem):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


        self.image = pygame.image.load(rf'C:\Users\icaro\PycharmProjects\DarkMonster\asset\assets\PNG\2\chao.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = WINDOW_HEIGHT+120
        self.rect.width = WINDOW_WIDTH

    def move(self):
       pass
