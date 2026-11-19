"""Modelo da oficina de jogos do IFMG. Setas movem | Espaço dispara | R reinicia"""
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
    pygame.display.set_caption('Jardim orbital')
    relogio = pygame.time.Clock()
    fonte = pygame.font.Font(None, 25)

    def escrever(texto, x=12, y=10):
        tela.blit(fonte.render(texto, True, TEXTO), (x, y))

    NAVE_VELOCIDADE = 5
    nave = pygame.Rect(300, 395, 40, 28)
    campo = pygame.Rect(0, 42, LARGURA, 390)
    tiros = []
    alvos = []
    pontos, vidas, espera = 0, 3, 0.5

    while True:
        dt = min(relogio.tick(60) / 1000, 0.04)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (
                evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                nave.centerx = 320
                tiros.clear()
                alvos.clear()
                pontos, vidas, espera = 0, 3, 0.5
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE and vidas > 0:
                tiros.append(pygame.Rect(nave.centerx - 3, nave.top - 12, 6, 12))

        teclas = pygame.key.get_pressed()

        # Atualize as regras antes de desenhar o quadro.
        if vidas > 0:
            nave.x += NAVE_VELOCIDADE * (teclas[pygame.K_RIGHT] - teclas[pygame.K_LEFT])
            nave.clamp_ip(campo)
            espera -= dt
            if espera <= 0:
                alvos.append(pygame.Rect(random.randint(5, 607), campo.top, 28, 28))
                espera = max(0.3, 0.9 - pontos * 0.025)
            for alvo in alvos:
                alvo.y += 3
            for tiro in tiros[:]:
                tiro.y -= 9
                atingido = tiro.collidelist(alvos)
                if atingido != -1:
                    alvos.pop(atingido)
                    tiros.remove(tiro)
                    pontos += 1
                elif tiro.bottom < campo.top:
                    tiros.remove(tiro)
            for alvo in alvos[:]:
                if alvo.colliderect(nave) or alvo.top > campo.bottom:
                    alvos.remove(alvo)
                    vidas = max(0, vidas - 1)

        tela.fill(FUNDO)
        pygame.draw.rect(tela, "#dce9fa", campo, 2)
        pygame.draw.polygon(tela, AZUL, [nave.midtop, nave.bottomleft, nave.bottomright])
        for alvo in alvos:
            pygame.draw.ellipse(tela, VERDE, alvo)
            pygame.draw.circle(tela, "#f6d665", alvo.center, 5)
        for tiro in tiros:
            pygame.draw.rect(tela, LARANJA, tiro, border_radius=3)
        escrever(f"Sementes coletadas: {pontos}  |  Vidas: {vidas}")
        if vidas == 0:
            escrever("Fim da rodada. Pressione R.", 210, 210)
        escrever('Setas movem | Espaço dispara | R reinicia', y=454)

        pygame.display.flip()


if __name__ == "__main__":
    main()
