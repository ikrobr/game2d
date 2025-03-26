import os
from codigo.Background import Background
from codigo.Chao import Chao
from codigo.Const import WINDOW_WIDTH, WINDOW_HEIGHT


class FactoryPerson:

    @staticmethod
    def get_personagem(personagem_name: str, position=(0, 0)):
        match personagem_name:
            case 'floresta':
                list_png = []
                for i in range(1,5):
                    nome_arquivo = rf'C:\Users\icaro\PycharmProjects\DarkMonster\asset\assets\PNG\2\floresta{i}.png'

                    if os.path.exists(nome_arquivo):
                        list_png.append(Background(f'floresta{i}', (0,0)))
                        list_png.append(Background(f'floresta{i}', (WINDOW_WIDTH,0)))
                    else:
                        print(f"img {nome_arquivo} não encontrada")

                chao_arquivo = r'C:\Users\icaro\PycharmProjects\DarkMonster\asset\assets\PNG\2\chao.png'
                if os.path.exists(chao_arquivo):
                    chao = Chao('chao', (0, WINDOW_HEIGHT - 50))  # Posição do chão
                    list_png.append(chao)
                else:
                    print(f"Imagem do chão NÃO encontrada: {chao_arquivo}")
                return list_png
