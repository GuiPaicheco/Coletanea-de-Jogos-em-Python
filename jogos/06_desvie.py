"""Modelo da oficina de jogos do IFMG. Setas movem | R reinicia"""
import random
import pygame

LARGURA, ALTURA = 640, 480
FUNDO = "#eef5ff"
AZUL = "#2354da"
LARANJA = "#df5340"
TEXTO = "#142443"


def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('Desvie dos obstáculos')
    relogio = pygame.time.Clock()
    fonte = pygame.font.Font(None, 25)

    def escrever(texto, x=12, y=10):
        tela.blit(fonte.render(texto, True, TEXTO), (x, y))

    jogador = pygame.Rect(299, 385, 42, 42)
    campo = pygame.Rect(0, 42, LARGURA, 398)
    obstaculos = []
    tempo, pontos, perdeu = 0.8, 0, False

    while True:
        dt = min(relogio.tick(60) / 1000, 0.04)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (
                evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                jogador.centerx = 320
                obstaculos.clear()
                tempo, pontos, perdeu = 0.8, 0, False

        teclas = pygame.key.get_pressed()

        # Atualize as regras antes de desenhar o quadro.
        if not perdeu:
            jogador.x += 5 * (teclas[pygame.K_RIGHT] - teclas[pygame.K_LEFT])
            jogador.clamp_ip(campo)
            tempo -= dt
            if tempo <= 0:
                largura = random.randint(28, 74)
                obstaculos.append(pygame.Rect(random.randrange(LARGURA-largura), campo.top, largura, 25))
                tempo = max(0.28, 0.9 - pontos * 0.02)
            for obstaculo in obstaculos[:]:
                obstaculo.y += min(10, 3 + pontos // 5)
                if obstaculo.colliderect(jogador):
                    perdeu = True
                    break
                if obstaculo.top >= campo.bottom:
                    obstaculos.remove(obstaculo)
                    pontos += 1

        tela.fill(FUNDO)
        pygame.draw.rect(tela, "#dce9fa", campo, 2)
        pygame.draw.rect(tela, AZUL, jogador, border_radius=12)
        for obstaculo in obstaculos:
            pygame.draw.rect(tela, LARANJA, obstaculo, border_radius=6)
        escrever(f"Obstáculos evitados: {pontos}")
        if perdeu:
            escrever("Colisão! Pressione R.", 230, 212)
        escrever('Setas movem | R reinicia', y=454)

        pygame.display.flip()


if __name__ == "__main__":
    main()
