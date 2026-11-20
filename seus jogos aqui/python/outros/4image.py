import pygame

pygame.init()
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
relogio = pygame.time.Clock()

# 1. Carrega a imagem (.convert_alpha() mantém a transparência e deixa o jogo mais rápido)
img_nave = pygame.image.load("teto.gif").convert_alpha()

# Opcional: Se a imagem vier gigante do Google, você redimensiona assim:
img_nave = pygame.transform.scale(img_nave, (50, 50))

# 2. Cria o Rect automaticamente com o tamanho (50x50) e já posiciona
rect_nave = img_nave.get_rect(center=(LARGURA // 2, ALTURA - 80))


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimentação (exatamente igual antes, mexendo no Rect!)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and rect_nave.left > 0:
        rect_nave.x -= 5
    if teclas[pygame.K_RIGHT] and rect_nave.right < LARGURA:
        rect_nave.x += 5

    # Desenho
    tela.fill((20, 20, 30))
    
    # 3. "Carimba" a imagem na posição exata onde está o Rect
    tela.blit(img_nave, rect_nave)
    tela.blit(img_nave, (100, 100))  # Exemplo de desenhar a mesma imagem em outro lugar

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()