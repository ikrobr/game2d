import pygame
from codigo.Personagem import Personagem

class Player(Personagem):
    def __init__(self, name: str, position: tuple = (0, 0)):
        super().__init__(name, position)
        self.surf = None
        self.rect = None

        try:
            self.surf = pygame.image.load(
                r'C:\Users\icaro\PycharmProjects\DarkMonster\asset\assets\PNG\2\Player1.png'
            ).convert_alpha()

            if self.surf:
                self.rect = self.surf.get_rect(topleft=position)
                print(f"Imagem carregada! Player1 Rect: {self.rect}")
            else:
                print("Erro ao carregar a imagem do jogador!")

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
