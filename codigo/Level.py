import pygame
from pygame import Surface, Rect
from pygame.font import Font

from codigo.Const import C_WHITE, WINDOW_HEIGHT, WINDOW_WIDTH
from codigo.FactoryPerson import FactoryPerson
from codigo.Personagem import Personagem
from codigo.Player import Player
from codigo.Background import Background


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.personagem_list: list[Personagem] = []

        # fundo e personagens
        self.personagem_list.extend(FactoryPerson.get_personagem('floresta'))
        self.player = FactoryPerson.get_personagem('Player1', position=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

        #tendo problemas com ordem de imgs renderizando, ajustar
        if self.player and self.player.surf and self.player.rect:
            self.personagem_list.append(self.player)
            print(f"Player1 criado com sucesso: {self.player} - Rect: {self.player.rect}")
        else:
            print("Erro ao carregar Player1!")
            self.player = None

        self.timeout = 20000

    def run(self):
        pygame.mixer_music.load(r'C:\Users\icaro\PycharmProjects\DarkMonster\asset\assets\\somlevel.wav')
        pygame.mixer_music.play(-1)
        running = True
        clock = pygame.time.Clock()

        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for pers in self.personagem_list:
                if isinstance(pers, Background): #desenhando paisagem
                    self.window.blit(pers.surf, pers.rect)

            if self.player:
                self.window.blit(self.player.surf, self.player.rect)
                print(f"Desenhando Player1 na posição {self.player.rect.topleft}") #d... player

            for pers in self.personagem_list:
                if not isinstance(pers, (Background, Player)):
                    if pers.surf and pers.rect:
                        self.window.blit(pers.surf, pers.rect)
                        pers.move()

            # Exibe informações na tela
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WINDOW_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.personagem_list)}', C_WHITE, (10, WINDOW_HEIGHT - 20))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

        pygame.display.flip()
