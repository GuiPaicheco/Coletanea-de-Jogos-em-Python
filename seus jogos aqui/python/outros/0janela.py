import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Janela Pygame")
relogio = pygame.time.Clock()

rodando = True
while rodando:
    # 1. Eventos (teclado, mouse, fechar janela)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # 2. Atualização de lógica (vazio por enquanto)

    # 3. Desenho na tela
    tela.fill((0, 67, 0)) # Preenche com RGB (Verde)
    pygame.display.flip() # Atualiza o frame na tela
    
    relogio.tick(60) # Trava o jogo em 60 FPS

pygame.quit()