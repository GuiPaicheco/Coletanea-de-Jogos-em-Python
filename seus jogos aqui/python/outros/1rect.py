import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Janela Pygame")
relogio = pygame.time.Clock()

# Cria um quadrado de 50x50 pixels na posição X=100, Y=200
x = 100
y = 200
meu_quadrado = pygame.Rect(x, y, 50, 50)
meu_quadrado2 = pygame.Rect(x, y, 50, 50)

rodando = True
while rodando:
    # 1. Eventos (teclado, mouse, fechar janela)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    tela.fill((2, 2, 2)) # Preenche com RGB (Verde)

    # Sintaxe: pygame.draw.rect(onde_desenhar, cor_RGB, objeto_rect)
    pygame.draw.rect(tela, (255, 0, 0), meu_quadrado)
    pygame.draw.rect(tela, (0, 0, 255), meu_quadrado2)

    x = x+1
    meu_quadrado.x = x
    meu_quadrado2.y = x

    # 3. Desenho na tela
    pygame.display.flip() # Atualiza o frame na tela
    
    relogio.tick(60) # Trava o jogo em 60 FPS

pygame.quit()