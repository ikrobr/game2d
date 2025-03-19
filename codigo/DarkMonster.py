import pygame


class Game:
    def __init__(self):
        pygame.init()  # iniciando pygame
        self.window = pygame.display.set_mode(size=(600, 490)) # pxs da janela

    def run(self):
        global TelaInicial
        while True:
            telaInicial = TelaInicial(self.window)
            telaInicial.run()
            pass
           # for event in pygame.event.get():
             #   if event.type == pygame.QUIT:
                #    pygame.quit()
                 #   quit()
