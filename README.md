# Coletânea de Jogos em Python

Modelos jogáveis feitos para os alunos da oficina **Criação de Jogos com Python** do IFMG, Campus Ibirité. Use os arquivos como ponto de partida para estudar, editar e criar suas próprias versões. Cada jogo roda em um único arquivo e usa apenas formas desenhadas pelo pygame-ce.

## Como rodar

Baixe a coletânea pelo botão **Code → Download ZIP**, extraia e abra um terminal na pasta extraída.

```powershell
py -m pip install -r requirements.txt
py jogos/06_desvie.py
```

Se o seu sistema usa `python3` ou `python`, substitua `py` pelo comando disponível nas duas linhas. A biblioteca instalada se chama `pygame-ce` e os exemplos usam `import pygame`.

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
