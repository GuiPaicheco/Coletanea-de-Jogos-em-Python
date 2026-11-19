# Coletânea de Jogos em Python

Repositório da oficina **Criação de Jogos com Python**, realizada na **Semana Nacional de Ciência e Tecnologia (SNCT)** do **IFMG – Campus Ibirité**, com Guilherme Paicheco e Ítalo Gabriel.

Na oficina, vamos usar a biblioteca **pygame-ce** para criar jogos em Python e simular como várias pessoas podem contribuir para um mesmo repositório no GitHub. Cada participante desenvolve seu próprio jogo e o compartilha com a turma em uma pasta própria.

| Pasta | O que você encontra |
| --- | --- |
| [jogos](jogos/) | Modelos jogáveis para testar, estudar e usar como ponto de partida. |
| [seus jogos aqui](seus%20jogos%20aqui/) | Espaço para publicar os jogos individuais criados durante a oficina. |

## Como participar

1. Explore os modelos em [jogos](jogos/) e escolha um para adaptar ou crie um jogo do zero.
2. No GitHub, clique em **Fork** para criar uma cópia do repositório na sua conta.
3. No seu fork, coloque os arquivos do jogo em uma subpasta com seu usuário, por exemplo, `seus jogos aqui/seu-usuario/nome-do-jogo/`. Inclua os controles e as instruções para rodar o jogo em um `README.md` dentro dessa subpasta.
4. Abra um **pull request** para este repositório. Informe o nome do jogo, como executá-lo e o que você testou. Os ministrantes podem revisar a contribuição e incorporá-la à coletânea.

## Como rodar um modelo

No Windows, abra o PowerShell na pasta do repositório e execute:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe jogos/06_desvie.py
```

Em macOS ou Linux, use `python3 -m venv .venv` no primeiro comando e `.venv/bin/python` no lugar de `.\.venv\Scripts\python.exe` nos demais.

## Escolha um modelo

| Opção da oficina | Arquivo | Primeira edição sugerida |
| --- | --- | --- |
| Pong • Rebote orbital | [01_rebote.py](jogos/01_rebote.py) | Mude a meta de pontos ou a regra de ponto duplo. |
| Snake • Cobra do pomar | [02_cobra.py](jogos/02_cobra.py) | Ajuste o intervalo entre os passos da cobra. |
| Flappy Bird simplificado • Voo do balão | [03_voo.py](jogos/03_voo.py) | Mude a abertura entre as barreiras. |
| Jogo da Velha | [04_jogo_da_velha.py](jogos/04_jogo_da_velha.py) | Experimente novas cores para o trio vencedor. |
| Space Shooter • Jardim orbital | [05_space_shooter.py](jogos/05_space_shooter.py) | Mude o número de vidas ou o ritmo de surgimento dos alvos. |
| Desvie dos Obstáculos | [06_desvie.py](jogos/06_desvie.py) | Mude a largura ou velocidade dos obstáculos. |
| Extra • Memória de cores | [07_memoria.py](jogos/07_memoria.py) | Ajuste por quanto tempo duas cartas ficam abertas. |
| Extra • Coleta contra o relógio | [08_coleta.py](jogos/08_coleta.py) | Mude a duração da rodada. |

Os controles aparecem na parte inferior de cada jogo. **R** reinicia a partida e **Esc** fecha a janela. Para editar, comece pelas constantes e procure o trecho que atualiza as regras antes do desenho.
