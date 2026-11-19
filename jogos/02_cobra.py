"""Modelo da oficina de jogos do IFMG. Setas | R reinicia"""
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
    pygame.display.set_caption('Cobra do pomar')
    relogio = pygame.time.Clock()
    fonte = pygame.font.Font(None, 25)

    def escrever(texto, x=12, y=10):
        tela.blit(fonte.render(texto, True, TEXTO), (x, y))

    COLUNAS, LINHAS, CELULA = 24, 16, 24
    origem = (32, 48)
    passo = 0.14
    direcoes = {
        pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1),
        pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0),
    }

    def novo_alimento(corpo):
        ocupadas = set(corpo)
        livres = [(x, y) for x in range(COLUNAS) for y in range(LINHAS)
                  if (x, y) not in ocupadas]
        return random.choice(livres) if livres else None

    def reiniciar():
        corpo = [(7, 8), (6, 8), (5, 8)]
        return corpo, novo_alimento(corpo), (1, 0), 0.0, "Jogando"

    corpo, alimento, direcao, tempo, estado = reiniciar()
    proxima = direcao

    while True:
        dt = min(relogio.tick(60) / 1000, 0.04)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (
                evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    corpo, alimento, direcao, tempo, estado = reiniciar()
                    proxima = direcao
                elif evento.key in direcoes:
                    candidata = direcoes[evento.key]
                    if candidata != (-direcao[0], -direcao[1]):
                        proxima = candidata


        # Atualize as regras antes de desenhar o quadro.
        if estado == "Jogando":
            tempo += dt
            if tempo >= passo:
                tempo -= passo
                direcao = proxima
                x, y = corpo[0]
                cabeca = (x + direcao[0], y + direcao[1])
                comeu = cabeca == alimento
                ocupadas = corpo if comeu else corpo[:-1]
                if not (0 <= cabeca[0] < COLUNAS and 0 <= cabeca[1] < LINHAS) or cabeca in ocupadas:
                    estado = "Colisão! R reinicia"
                else:
                    corpo.insert(0, cabeca)
                    if comeu:
                        alimento = novo_alimento(corpo)
                        if alimento is None:
                            estado = "Pomar completo! R reinicia"
                    else:
                        corpo.pop()

        tela.fill(FUNDO)
        pygame.draw.rect(tela, "#dce9fa", (*origem, COLUNAS*CELULA, LINHAS*CELULA))
        for indice, (x, y) in enumerate(corpo):
            pygame.draw.rect(tela, AZUL if indice == 0 else VERDE,
                             (origem[0]+x*CELULA+1, origem[1]+y*CELULA+1, 22, 22), border_radius=6)
        if alimento is not None:
            x, y = alimento
            pygame.draw.circle(tela, LARANJA, (origem[0]+x*CELULA+12, origem[1]+y*CELULA+12), 8)
        escrever(f"Frutas: {len(corpo)-3}  |  {estado}")
        escrever('Setas | R reinicia', y=454)

        pygame.display.flip()


if __name__ == "__main__":
    main()
