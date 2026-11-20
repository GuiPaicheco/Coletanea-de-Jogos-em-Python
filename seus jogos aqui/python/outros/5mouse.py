import pygame

pygame.init()
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
relogio = pygame.time.Clock()

# Jogador no centro da tela
jogador = pygame.Rect(400, 300, 30, 30)
balas = []

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
        # Dispara ao clicar com o botão esquerdo do mouse (botão 1)
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            pos_mouse = pygame.math.Vector2(pygame.mouse.get_pos())
            pos_jogador = pygame.math.Vector2(jogador.center)
            
            # Calcula o vetor direção (Destino - Origem)
            direcao = pos_mouse - pos_jogador
            
            # Evita erro de divisão por zero se clicar exatamente no centro do jogador
            if direcao.length() > 0:
                velocidade_bala = 10
                # .normalize() deixa o vetor com tamanho 1, depois multiplicamos pela velocidade
                vetor_vel = direcao.normalize() * velocidade_bala
                
                balas.append({
                    "pos": pos_jogador.copy(), # Guarda posição em float (Vector2 aceita decimais!)
                    "vel": vetor_vel,
                    "rect": pygame.Rect(jogador.centerx, jogador.centery, 8, 8)
                })

    # Atualiza as balas
    for bala in balas[:]:
        bala["pos"] += bala["vel"] # Soma vetorial direta (X e Y ao mesmo tempo!)
        bala["rect"].center = (int(bala["pos"].x), int(bala["pos"].y))
        
        if not tela.get_rect().colliderect(bala["rect"]):
            balas.remove(bala)

    # --- DESENHO ---
    tela.fill((20, 20, 30))
    
    # Linha de mira visual (ajuda muito os alunos a verem o vetor funcionando!)
    pos_mouse = pygame.mouse.get_pos()
    pygame.draw.line(tela, (80, 80, 100), jogador.center, pos_mouse, 2)
    
    # Desenha jogador e balas
    pygame.draw.rect(tela, (50, 150, 255), jogador)
    for bala in balas:
        pygame.draw.circle(tela, (255, 220, 50), bala["rect"].center, 5)

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()