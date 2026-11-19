"""Modelo da oficina de jogos do IFMG. Clique para revelar | R reinicia"""
import random
import pygame

LARGURA, ALTURA = 640, 480
FUNDO = "#eef5ff"
TEXTO = "#142443"


def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('Memória de cores')
    relogio = pygame.time.Clock()
    fonte = pygame.font.Font(None, 25)

    def escrever(texto, x=12, y=10):
        tela.blit(fonte.render(texto, True, TEXTO), (x, y))

    CORES = ["#e3426b", "#2354da", "#127d67", "#f0ae24", "#7750c5", "#e47035"]
    cartas = [pygame.Rect(115+i%4*105, 65+i//4*117, 94, 104) for i in range(12)]
    valores = list(range(6)) * 2
    random.shuffle(valores)
    abertas = []
    pares = set()
    espera = 0.0
    tentativas = 0

    while True:
        dt = min(relogio.tick(60) / 1000, 0.04)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (
                evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                random.shuffle(valores)
                abertas.clear()
                pares.clear()
                espera, tentativas = 0.0, 0
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and len(abertas) < 2:
                for i, carta in enumerate(cartas):
                    if carta.collidepoint(evento.pos) and i not in pares and i not in abertas:
                        abertas.append(i)
                        if len(abertas) == 2:
                            tentativas += 1
                            a, b = abertas
                            if valores[a] == valores[b]:
                                pares.update(abertas)
                                abertas.clear()
                            else:
                                espera = 0.65
                        break


        # Atualize as regras antes de desenhar o quadro.
        if espera > 0:
            espera -= dt
            if espera <= 0:
                abertas.clear()

        tela.fill(FUNDO)
        for i, carta in enumerate(cartas):
            pygame.draw.rect(tela, "#d0e1f7", carta, border_radius=12)
            if i in abertas or i in pares:
                pygame.draw.circle(tela, CORES[valores[i]], carta.center, 25)
                simbolo = fonte.render(str(valores[i] + 1), True, "white")
                tela.blit(simbolo, simbolo.get_rect(center=carta.center))
            else:
                pygame.draw.circle(tela, "#aac7ec", carta.center, 10, 2)
        escrever(f"Tentativas: {tentativas}  |  Pares: {len(pares)//2}/6")
        if len(pares) == 12:
            escrever("Todos os pares! R reinicia.", 400)
        escrever('Clique para revelar | R reinicia', y=454)

        pygame.display.flip()


if __name__ == "__main__":
    main()
