import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Janela Pygame")
relogio = pygame.time.Clock()

x = 100
y = 200
player = pygame.Rect(x, y, 50, 50)

rodando = True
while rodando:
    # 1. Eventos (teclado, mouse, fechar janela)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill((2, 2, 2)) # Preenche com RGB

    # 2. Atualização de lógica (vazio por enquanto)
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:  # Seta para a esquerda
        player.x -= 5
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]: # Seta para a direita
        player.x += 5
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:    # Seta para cima
        player.y -= 5
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:  # Seta para baixo
        player.y += 5

    # 3. Desenho na tela
    pygame.draw.rect(tela, (255, 0, 0), player)
    pygame.display.flip() # Atualiza o frame na tela
    
    relogio.tick(60) # Trava o jogo em 60 FPS

pygame.quit()