"""Modelo da oficina de jogos do IFMG. Clique para jogar | R reinicia"""
import pygame

LARGURA, ALTURA = 640, 480
FUNDO = "#eef5ff"
AZUL = "#2354da"
VERDE = "#127d67"
TEXTO = "#142443"


def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('Jogo da velha')
    relogio = pygame.time.Clock()
    fonte = pygame.font.Font(None, 25)

    def escrever(texto, x=12, y=10):
        tela.blit(fonte.render(texto, True, TEXTO), (x, y))

    TABULEIRO = pygame.Rect(140, 57, 360, 360)
    CELULA = 120
    LINHAS = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7),
              (2,5,8), (0,4,8), (2,4,6)]
    casas = [None] * 9
    turno = "X"
    vencedora = None
    empate = False

    while True:
        relogio.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (
                evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                casas = [None] * 9
                turno = "X"
                vencedora = None
                empate = False
            if (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1
                    and not vencedora and not empate and TABULEIRO.collidepoint(evento.pos)):
                x, y = evento.pos
                coluna = (x - TABULEIRO.x) // CELULA
                linha = (y - TABULEIRO.y) // CELULA
                indice = linha * 3 + coluna
                if casas[indice] is None:
                    casas[indice] = turno
                    vencedora = next((trio for trio in LINHAS if all(casas[i] == turno for i in trio)), None)
                    empate = vencedora is None and all(casa is not None for casa in casas)
                    if not vencedora and not empate:
                        turno = "O" if turno == "X" else "X"


        tela.fill(FUNDO)
        for i, marca in enumerate(casas):
            caixa = pygame.Rect(TABULEIRO.x + i % 3 * CELULA, TABULEIRO.y + i // 3 * CELULA, CELULA, CELULA)
            pygame.draw.rect(tela, "#fde6a7" if vencedora and i in vencedora else "#dce9fa",
                             caixa.inflate(-5, -5), border_radius=12)
            x, y = caixa.center
            if marca == "X":
                pygame.draw.line(tela, AZUL, (x-24, y-24), (x+24, y+24), 7)
                pygame.draw.line(tela, AZUL, (x-24, y+24), (x+24, y-24), 7)
            elif marca == "O":
                pygame.draw.circle(tela, VERDE, caixa.center, 29, 7)
        escrever(f"{turno} venceu" if vencedora else "Empate" if empate else f"Vez de {turno}")
        escrever('Clique para jogar | R reinicia', y=454)

        pygame.display.flip()


if __name__ == "__main__":
    main()
