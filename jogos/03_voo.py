"""Modelo da oficina de jogos do IFMG. Espaço impulsiona | R reinicia"""
import random
import pygame

LARGURA, ALTURA = 640, 480
FUNDO = "#eef5ff"
AZUL = "#2354da"
VERDE = "#127d67"
LARANJA = "#df5340"
TEXTO = "#142443"


def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('Voo do balão')
    relogio = pygame.time.Clock()
    fonte = pygame.font.Font(None, 25)

    def escrever(texto, x=12, y=10):
        tela.blit(fonte.render(texto, True, TEXTO), (x, y))

    GRAVIDADE, IMPULSO, VELOCIDADE = 760, -305, 192
    LARGURA_BARREIRA, VAO = 44, 155
    balao = pygame.Rect(122, 218, 27, 32)
    limite = pygame.Rect(0, 43, 640, 391)

    def reiniciar():
        return 218.0, 0.0, [], 0.3, 0, "Pressione espaço"

    y, vy, barreiras, espera, pontos, estado = reiniciar()

    while True:
        dt = min(relogio.tick(60) / 1000, 0.04)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (
                evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                y, vy, barreiras, espera, pontos, estado = reiniciar()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE and estado != "Colisão":
                estado = "Voando"
                vy = IMPULSO


        # Atualize as regras antes de desenhar o quadro.
        if estado == "Voando":
            vy += GRAVIDADE * dt
            y += vy * dt
            espera -= dt
            if espera <= 0:
                barreiras.append([float(LARGURA), random.randint(150, 318), False])
                espera = 1.55
        balao.y = round(y)
        pecas = []
        for barreira in barreiras:
            if estado == "Voando":
                barreira[0] -= VELOCIDADE * dt
            x, centro, contou = barreira
            inicio = centro - VAO // 2
            fim = inicio + VAO
            pecas.extend([pygame.Rect(round(x), limite.top, LARGURA_BARREIRA, inicio-limite.top),
                          pygame.Rect(round(x), fim, LARGURA_BARREIRA, limite.bottom-fim)])
            if estado == "Voando" and not contou and x + LARGURA_BARREIRA < balao.left:
                pontos += 1
                barreira[2] = True
        barreiras = [b for b in barreiras if b[0] + LARGURA_BARREIRA > 0]
        if not limite.contains(balao) or balao.collidelist(pecas) != -1:
            estado = "Colisão"

        tela.fill(FUNDO)
        pygame.draw.rect(tela, "#dce9fa", limite, 2)
        for peca in pecas:
            pygame.draw.rect(tela, AZUL, peca, border_radius=6)
        pygame.draw.ellipse(tela, LARANJA, balao.inflate(0, -7).move(0, -3))
        pygame.draw.rect(tela, VERDE, (balao.centerx-5, balao.bottom-8, 10, 8), border_radius=2)
        escrever(f"Vãos: {pontos}  |  {estado}")
        escrever('Espaço impulsiona | R reinicia', y=454)

        pygame.display.flip()


if __name__ == "__main__":
    main()
