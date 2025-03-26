import os
from codigo.Background import Background
from codigo.Const import WINDOW_WIDTH


class FactoryPerson:

    @staticmethod
    def get_personagem(personagem_name: str, position=(0, 0)):
        match personagem_name:
            case 'floresta':
                list_png = []
                for i in range(1,4):
                    nome_arquivo = rf'C:\Users\icaro\PycharmProjects\DarkMonster\asset\assets\PNG\2\floresta{i}.png'

                    if os.path.exists(nome_arquivo):
                        list_png.append(Background(f'floresta{i}', (0,0)))
                        list_png.append(Background(f'floresta{i}', (WINDOW_WIDTH,0)))
                    else:
                        print(f"img {nome_arquivo} não encontrada")

                return list_png
