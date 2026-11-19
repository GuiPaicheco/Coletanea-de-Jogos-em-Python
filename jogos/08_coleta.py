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
    pygame.display.set_caption('Coleta contra o relógio')
    relogio = pygame.time.Clock()
    fonte = pygame.font.Font(None, 25)

    def escrever(texto, x=12, y=10):
        tela.blit(fonte.render(texto, True, TEXTO), (x, y))

    DURACAO = 18.0
    campo = pygame.Rect(0, 41, 640, 396)
    jogador = pygame.Rect(307, 226, 26, 26)

    def nova_estrela():
        return pygame.Rect(random.randint(12, 606), random.randint(54, 405), 20, 20)

    estrela = nova_estrela()
    tempo = DURACAO
    pontos = 0

    while True:
        dt = min(relogio.tick(60) / 1000, 0.04)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (
                evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                jogador.center = campo.center
                estrela = nova_estrela()
                tempo = DURACAO
                pontos = 0

        teclas = pygame.key.get_pressed()

        # Atualize as regras antes de desenhar o quadro.
        if tempo > 0:
            tempo = max(0, tempo - dt)
            jogador.x += 5 * (teclas[pygame.K_RIGHT] - teclas[pygame.K_LEFT])
            jogador.y += 5 * (teclas[pygame.K_DOWN] - teclas[pygame.K_UP])
            jogador.clamp_ip(campo)
            if jogador.colliderect(estrela):
                pontos += 1
                estrela = nova_estrela()
                while jogador.colliderect(estrela):
                    estrela = nova_estrela()

        tela.fill(FUNDO)
        pygame.draw.rect(tela, "#dce9fa", campo, 2)
        pygame.draw.rect(tela, AZUL, jogador, border_radius=7)
        x, y = estrela.center
        pygame.draw.polygon(tela, LARANJA, [(x, y-10), (x+10, y), (x, y+10), (x-10, y)])
        escrever(f"Coletados: {pontos}  |  Tempo: {tempo:.1f} s")
        if tempo == 0:
            escrever("Tempo encerrado! Pressione R.", 195, 185)
        escrever('Setas movem | R reinicia', y=454)

        pygame.display.flip()


if __name__ == "__main__":
    main()
