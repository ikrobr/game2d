from codigo.Personagem import Personagem


class Background(Personagem):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self,):
        pass