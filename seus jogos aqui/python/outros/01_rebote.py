"""Modelo da oficina de jogos do IFMG. W/S e setas | R reinicia"""
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
    pygame.display.set_caption('Rebote orbital')
    relogio = pygame.time.Clock()
    fonte = pygame.font.Font(None, 25)

    def escrever(texto, x=12, y=10):
        tela.blit(fonte.render(texto, True, TEXTO), (x, y))

    raquete_esq = pygame.Rect(35, 190, 16, 90)
    raquete_dir = pygame.Rect(589, 190, 16, 90)
    quadra = pygame.Rect(0, 39, LARGURA, 398)
    bola = pygame.Vector2(320, 230)
    velocidade = pygame.Vector2(280, 120)
    pontos = [0, 0]
    rebotes = 0
    META = 7

    while True:
        dt = min(relogio.tick(60) / 1000, 0.04)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (
                evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                pontos = [0, 0]
                rebotes = 0
                bola.update(320, 230)
                velocidade.update(280, 120)

        teclas = pygame.key.get_pressed()

        # Atualize as regras antes de desenhar o quadro.
        if max(pontos) < META:
            raquete_esq.y += (teclas[pygame.K_s] - teclas[pygame.K_w]) * 5
            raquete_dir.y += (teclas[pygame.K_DOWN] - teclas[pygame.K_UP]) * 5
            raquete_esq.clamp_ip(quadra)
            raquete_dir.clamp_ip(quadra)
            bola += velocidade * dt
            if bola.y < 50 or bola.y > 426:
                bola.y = max(50, min(426, bola.y))
                velocidade.y *= -1
            caixa = pygame.Rect(round(bola.x)-9, round(bola.y)-9, 18, 18)
            raquete = raquete_esq if velocidade.x < 0 else raquete_dir
            if caixa.colliderect(raquete):
                bola.x = raquete.right + 9 if velocidade.x < 0 else raquete.left - 9
                velocidade.x *= -1
                velocidade.y = (bola.y - raquete.centery) * 5
                rebotes += 1
            if bola.x < -9 or bola.x > LARGURA + 9:
                lado = int(bola.x < 0)
                pontos[lado] += 2 if rebotes >= 4 else 1
                rebotes = 0
                bola.update(320, 230)
                velocidade.update(280 if lado == 0 else -280, 120)

        tela.fill(FUNDO)
        pygame.draw.rect(tela, "#c9ddfa", quadra, 2)
        pygame.draw.line(tela, "#c9ddfa", (320, 39), (320, 437), 2)
        pygame.draw.rect(tela, AZUL, raquete_esq, border_radius=7)
        pygame.draw.rect(tela, VERDE, raquete_dir, border_radius=7)
        pygame.draw.circle(tela, LARANJA, bola, 9)
        escrever(f"{pontos[0]} × {pontos[1]}  |  {rebotes} rebotes (4+ valem ponto duplo)")
        if max(pontos) >= META:
            escrever("Fim da rodada! Pressione R.", 208, 205)
        escrever('W/S e setas | R reinicia', y=454)

        pygame.display.flip()


if __name__ == "__main__":
    main()
