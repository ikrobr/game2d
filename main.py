import pygame

print('Iniciando Janela')
pygame.init() #iniciando pygame

window = pygame.display.set_mode(size = (600, 490))
print('Finalizando Janela')

print('Loop Manter Janela')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()