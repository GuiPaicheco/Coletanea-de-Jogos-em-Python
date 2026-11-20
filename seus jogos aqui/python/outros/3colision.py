import pygame
import random

pygame.init()
janela = (800, 600)
tela = pygame.display.set_mode(janela)
pygame.display.set_caption("Janela Pygame")
relogio = pygame.time.Clock()

x = 100
y = 200
player = pygame.Rect(x, y, 50, 50)

inimigos = []
timer = 0
meta = 100

cor = (2, 2, 2)

def mover_jogador():
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:  # Seta para a esquerda
        player.x -= 5
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]: # Seta para a direita
        player.x += 5
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:    # Seta para cima
        player.y -= 5
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:  # Seta para baixo
        player.y += 5

def criar_inimigo():
    x = random.randint(0, janela[0] - 50)
    inimigo = pygame.Rect(x, janela[1], 50, 50)
    inimigos.append(inimigo)

def mover_inimigos():
    for inimigo in inimigos:
        inimigo.y -= 5
        if inimigo.y < 0:
            inimigos.remove(inimigo)

def desenhar():
    tela.fill(cor) # Preenche com RGB
    pygame.draw.rect(tela, (255, 0, 0), player)
    for inimigo in inimigos:
        pygame.draw.rect(tela, (0, 255, 0), inimigo)

    
    pygame.display.flip() # Atualiza o frame na tela


rodando = True
while rodando:
    # 1. Eventos (teclado, mouse, fechar janela)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    

    # 2. Atualização de lógica (vazio por enquanto)
    if timer > meta+random.randint(10, 20): # A cada 60 frames (1 segundo)
        criar_inimigo()
        timer = 0
        meta = max(0,meta-5)
    else:
        timer+=1
    mover_jogador()
    mover_inimigos()
    if player.collidelist(inimigos) != -1:
        print("Colisão detectada!")
        cor = (0, 255, 0)
        rodando = False
    desenhar()
    
    relogio.tick(60) # Trava o jogo em 60 FPS

pygame.quit()