import os
from codigo.Background import Background
from codigo.Chao import Chao
from codigo.Const import WINDOW_WIDTH, WINDOW_HEIGHT
from codigo.Player import Player


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
                    chao1 = Chao('chao', (0, WINDOW_HEIGHT))
                    chao2 = Chao('chao', (WINDOW_WIDTH, WINDOW_HEIGHT))
                    list_png.append(chao1)
                    list_png.append(chao2)
                return list_png

            case 'Player1':
                print("Criando Player1")
                player_instance = Player(name='Player1', position=position)

                if player_instance and player_instance.rect:
                    #TESTE print(f"Player1 criado com sucesso: {player_instance} - Rect: {player_instance.rect}")
                    return player_instance
                else:
                    #TESTE print("Erro ao criar Player1! Rect não foi inicializado corretamente.")
                    return None