import pygame

from codigo.Const import WINDOW_HEIGHT
from codigo.Personagem import Personagem
from codigo.Tiro import Tiro


class Player(Personagem):
    def __init__(self, name: str, position: tuple = (0, 0)):
        super().__init__(name, position)
        self.surf = None
        self.rect = None
        self.tiro = []

        try:
            self.surf = pygame.image.load(
                r'C:\Users\icaro\PycharmProjects\DarkMonster\asset\assets\PNG\2\Player1.png'
            ).convert_alpha()

            novo_tamanho = (self.surf.get_width() // 5, self.surf.get_height() // 4)  #arrumei o tamanho
            self.surf = pygame.transform.smoothscale(self.surf, novo_tamanho)


            if self.surf:
                self.rect = self.surf.get_rect(midleft=(0, WINDOW_HEIGHT - self.surf.get_height() // 1+20))
            else:
                print("Erro ao carregar a imagem do player!")

        except pygame.error as e:
            print(f"Erro ao carregar a imagem: {e}")
            self.surf = None

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

    def shoot(self):
        """Dispara uma bala da posição do tanque"""
        tiro = Tiro(self.rect.midright)  # Dispara da parte direita do tanque
        self.tiro.append(tiro)  # Adiciona a bala à lista de balas