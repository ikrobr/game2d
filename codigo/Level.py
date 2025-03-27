import pygame
from codigo.Background import Background
from codigo.Const import C_WHITE, WINDOW_WIDTH, WINDOW_HEIGHT
from codigo.FactoryPerson import FactoryPerson
from codigo.Inimigos import Inimigos
from codigo.Personagem import Personagem
from codigo.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.personagem_list: list[Personagem] = []
        self.personagem_list.extend(FactoryPerson.get_personagem('floresta'))
        self.player = FactoryPerson.get_personagem('Player1', position=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

        if self.player and self.player.surf and self.player.rect:
            self.personagem_list.append(self.player)
        else:
            print("Erro ao carregar Player1!")
            self.player = None

        self.timeout = 20000
        self.pontuacao = 0

        self.inimigos_list = [
            Inimigos('Inimigo1', position=(WINDOW_WIDTH, WINDOW_HEIGHT - 80), velocidade=3),
        ]
        self.personagem_list.extend(self.inimigos_list)

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
                if isinstance(pers, Background):
                    pers.move()
                    self.window.blit(pers.surf, pers.rect)

            if self.player:
                self.window.blit(self.player.surf, self.player.rect)

            for pers in self.personagem_list:
                if not isinstance(pers, (Background, Player)):
                    if pers.surf and pers.rect:
                        self.window.blit(pers.surf, pers.rect)
                        pers.move()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.player.shoot()

            for tiro in self.player.tiro[:]:
                tiro.move()
                self.window.blit(tiro.surf, tiro.rect)

                if tiro.off_screen(WINDOW_WIDTH):
                    self.player.tiro.remove(tiro)

            for tiro in self.player.tiro[:]:
                for inimigo in self.inimigos_list[:]:
                    if tiro.rect.colliderect(inimigo.rect):
                        self.inimigos_list.remove(inimigo)
                        self.player.tiro.remove(tiro)
                        self.pontuacao += 10
                       #TESTE print(f"Colisão detectada! Pontuação: {self.pontuacao}")

            self.level_text(20, f'Pontuação: {self.pontuacao}', C_WHITE, (10, 5))

            if self.pontuacao >= 1000:
                running = False

            pygame.display.flip()

        self.salvar_pontuacao()

    def level_text(self, size, text, color, position):
        text_font = pygame.font.SysFont(name="Courier", size=size, bold=True)
        text_surf = text_font.render(text, True, color)
        text_rect = text_surf.get_rect(topleft=position)
        self.window.blit(text_surf, text_rect)

    def salvar_pontuacao(self):
        try:
            with open('rank.txt', 'a') as f:
                f.write(f"{self.pontuacao}\n")
        except Exception as e:
            print(f"Erro ao salvar pontuação: {e}")
