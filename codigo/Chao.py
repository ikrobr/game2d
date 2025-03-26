import pygame

from codigo.Const import WINDOW_HEIGHT, WINDOW_WIDTH
from codigo.Personagem import Personagem


class Chao(Personagem):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.image = pygame.image.load(r'C:\Users\icaro\PycharmProjects\DarkMonster\asset\assets\PNG\2\chao.png')
        self.rect = self.image.get_rect()


        self.rect.bottom = WINDOW_HEIGHT + 110
        self.rect.width = WINDOW_WIDTH
        self.rect.x = position[0]
    def move(self):
        self.rect.x -= 2

        if self.rect.right <= 0:
            self.rect.left = WINDOW_WIDTH
