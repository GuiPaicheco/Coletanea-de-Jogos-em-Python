import pygame
import random

pygame.init()
LARGURA, ALTURA = 1200,900 #800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
relogio = pygame.time.Clock()
# Usa a fonte padrão do sistema (None) no tamanho 36
fonte = pygame.font.SysFont(None, 36)
pygame.mixer.init() # Garante que o sistema de som iniciou

# carregar imagens
SprJogador = pygame.image.load("teto.gif").convert_alpha()
SprJogador = pygame.transform.scale(SprJogador, (50, 50))
SprVermelho = pygame.image.load("BalaoVermelho.png").convert_alpha()
SprVermelho = pygame.transform.scale(SprVermelho, (40, 50))
SprVerde = pygame.image.load("BalaoVerde.png").convert_alpha()
SprVerde = pygame.transform.scale(SprVerde, (40, 50))
SprAzul = pygame.image.load("BalaoAzul.png").convert_alpha()
SprAzul = pygame.transform.scale(SprAzul, (40, 50))
SprAmarelo = pygame.image.load("BalaoAmarelo.png").convert_alpha()
SprAmarelo = pygame.transform.scale(SprAmarelo, (40, 50))

# sons do jogo
pop = pygame.mixer.Sound("pop.mp3")
pop.set_volume(0.4)

# Lista de atores
inimigos = []
balas = []
# 2. Cria o Rect automaticamente com o tamanho (50x50) e já posiciona
Jogador = SprJogador.get_rect(center=(LARGURA // 2, ALTURA - 80))

# Variaveis de jogo
pontos = 0
delay = 0

def mover_jogador():
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and Jogador.left > 0:
        Jogador.x -= 5
    if teclas[pygame.K_RIGHT] and Jogador.right < LARGURA:
        Jogador.x += 5
    if teclas[pygame.K_UP] and Jogador.top > 0:
        Jogador.y -= 5
    if teclas[pygame.K_DOWN] and Jogador.bottom < ALTURA:
        Jogador.y += 5

def criar_inimigo():
    lado = random.randint(0, 3)
    speed = 2
    match lado:
        case 0: # cima
            x = random.randint(0, LARGURA - 40)
            pos = (x, -50)
        case 1: # direita
            y = random.randint(0, ALTURA - 50)
            pos = (LARGURA, y)
        case 2: # baixo
            x = random.randint(0, LARGURA - 40)
            pos = (x, ALTURA)
        case 3: # esquerda
            y = random.randint(0, ALTURA - 50)
            pos = (-50, y)
    vida = random.randint(1, 4)
    if vida == 4:
        speed = 4
    if vida == 1:
        speed = 1
    inimigos.append({
                "vida": vida,
                "speed": speed,
                "rect": pygame.Rect(pos[0], pos[1], 40, 50)
            })

def mover_inimigos():
    for inimigo in inimigos:
        if inimigo["rect"].top < Jogador.top - 20:
            inimigo["rect"].y += inimigo["speed"]
        elif inimigo["rect"].top > Jogador.top + 20:
            inimigo["rect"].y -= inimigo["speed"]
        if inimigo["rect"].left < Jogador.left - 20:
            inimigo["rect"].x += inimigo["speed"]
        elif inimigo["rect"].left > Jogador.left:
            inimigo["rect"].x -= inimigo["speed"]

def mover_balas():
    global pontos
    for bala in balas[:]:
        bala["pos"] += bala["vel"]
        bala["rect"].center = (int(bala["pos"].x), int(bala["pos"].y))

        # 1. Remove se saiu da tela
        if not tela.get_rect().colliderect(bala["rect"]):
            balas.remove(bala)
            continue # Pula para a próxima bala, pois essa já foi removida

        # 2. Testa colisão percorrendo os dicionários de inimigos
        for inimigo in inimigos[:]:
            if bala["rect"].colliderect(inimigo["rect"]):
                balas.remove(bala)
                inimigo["vida"] -= 1
                pontos += 1
                pop.play()
                #reduzir speed amarelo
                if inimigo["vida"] == 3:
                    inimigo["speed"] = 2
                #reduzir speed para vermelho
                if inimigo["vida"] == 1:
                    inimigo["speed"] = 1
                #matar inimgo                
                if inimigo["vida"] <= 0:
                    inimigos.remove(inimigo)
                break # Para o loop de inimigos pois essa bala já acertou um alvo

def colisao():
    for inimigo in inimigos:
        if inimigo["rect"].colliderect(Jogador):
            print("Colisão detectada!")
            return True
    return False

def carimbar_imagens():
    tela.fill((20, 20, 30))
    tela.blit(SprJogador, Jogador)
    for inimigo in inimigos:
        if inimigo["vida"] == 1:
            tela.blit(SprVermelho, inimigo["rect"])
        elif inimigo["vida"] == 2:
            tela.blit(SprAzul, inimigo["rect"])
        elif inimigo["vida"] == 3:
            tela.blit(SprVerde, inimigo["rect"])
        elif inimigo["vida"] == 4:
            tela.blit(SprAmarelo, inimigo["rect"])
    for bala in balas:
        pygame.draw.circle(tela, (255, 220, 50), bala["rect"].center, 5)
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, (255, 255, 255))
    tela.blit(texto_pontos, (15, 15)) # Desenha no canto superior esquerdo

def atirar():
    pos_mouse = pygame.math.Vector2(pygame.mouse.get_pos())
    pos_jogador = pygame.math.Vector2(Jogador.center)
    # Calcula o vetor direção (Destino - Origem)
    direcao = pos_mouse - pos_jogador
    
    # Evita erro de divisão por zero se clicar exatamente no centro do Jogador
    if direcao.length() > 0:
        velocidade_bala = 10
        # .normalize() deixa o vetor com tamanho 1, depois multiplicamos pela velocidade
        vetor_vel = direcao.normalize() * velocidade_bala
        
        balas.append({
            "pos": pos_jogador.copy(), # Guarda posição em float (Vector2 aceita decimais!)
            "vel": vetor_vel,
            "rect": pygame.Rect(Jogador.centerx, Jogador.centery, 8, 8)
        })

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            atirar()

    if colisao(): rodando = False
    if delay > 50:
        delay = 0
        criar_inimigo()
    else: delay += 1
    
    mover_jogador()
    mover_balas()
    mover_inimigos()
    carimbar_imagens()

    pygame.display.flip()
    relogio.tick(60)

print(f"pontos: ",pontos)
pygame.quit()