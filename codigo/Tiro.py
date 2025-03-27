import pygame

class Tiro:
    def __init__(self, position: tuple, speed: int = 10):
        self.surf = pygame.image.load(
            r'C:\Users\icaro\PycharmProjects\DarkMonster\asset\assets\PNG\2\tiro1.png'
        ).convert_alpha()

        self.surf = pygame.transform.scale(self.surf, (10, 5))  # Ajusta o tamanho da bala
        self.rect = self.surf.get_rect(midleft=position)  # Define a posição inicial
        self.speed = speed  # Velocidade da bala

    def move(self):
        """Move a bala para a direita"""
        self.rect.x += self.speed

    def off_screen(self, width):
        """Verifica se a bala saiu da tela"""
        return self.rect.left > width
