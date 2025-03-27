import pygame.image

from codigo.Const import WINDOW_HEIGHT
from codigo.Personagem import Personagem


class Inimigos(Personagem):
    def __init__(self, name: str,position: tuple = (0, 0), velocidade: int = 2):
        super().__init__(name, position)
        self.surf = None
        self.velocidade = velocidade
        self.rect = None

        self.surf = pygame.image.load(r'C:\Users\icaro\PycharmProjects\DarkMonster\asset\assets\PNG\2\Inimigo1.png').convert_alpha()

        novo_tamanho = (self.surf.get_width() // 8, self.surf.get_height() // 8)  # arrumei o tamanho
        self.surf = pygame.transform.smoothscale(self.surf, novo_tamanho)

        if self.surf:
            self.rect = self.surf.get_rect(midleft=(0, WINDOW_HEIGHT - self.surf.get_height() // 1+52))
        else:
            print("Erro img")



    def move(self):

        self.rect.x -= self.velocidade  #para a esquerda

        if self.rect.right < 0:
            self.rect.left = 690  #borda direita