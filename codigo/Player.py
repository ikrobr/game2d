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
        self.pontos = 0

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
        #disparo
        tiro = Tiro(self.rect.midright)  # Dispara da parte direita do tanque
        self.tiro.append(tiro)  #add

    def checar_colisao(self, inimigos):
        for tiro in self.tiro[:]:
            for inimigo in inimigos:
                if inimigo.colide(tiro):
                    self.tiro.remove(tiro)
                    inimigos.remove(inimigo)
                    self.pontos += 10
                    return True
        return False

    def checar_game_over(self, inimigos):
        for inimigo in inimigos:
            if inimigo.rect.colliderect(self.rect):  #inimigo chegar ao tanque
                return True  # Game over
        return False