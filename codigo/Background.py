from codigo.Const import WINDOW_WIDTH, OBJ_SPEED
from codigo.Personagem import Personagem


class Background(Personagem):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self,):
        self.rect.centerx -= 0.7
        if self.rect.right <= 0:
            self.rect.left = WINDOW_WIDTH