import pygame

class Tiro:
    def __init__(self, position: tuple, speed: int = 10):
        self.surf = pygame.image.load(
            r'C:\Users\icaro\PycharmProjects\DarkMonster\asset\assets\PNG\2\tiro1.png'
        ).convert_alpha()

        self.surf = pygame.transform.scale(self.surf, (15, 10))  #tamanho do tiro

        position = (position[0], position[1] - 25)
        self.rect = self.surf.get_rect(midleft=position) #posição do tiro
        self.speed = speed  # Velocidade da bala

    def move(self):
        self.rect.x += self.speed

    def off_screen(self, width):
        return self.rect.left > width
