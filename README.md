# Coletânea de Jogos em Python

Modelos jogáveis feitos para os alunos da oficina **Criação de Jogos com Python** do IFMG, Campus Ibirité. Use os arquivos como ponto de partida para estudar, editar e criar suas próprias versões. Cada jogo roda em um único arquivo e usa apenas formas desenhadas pelo pygame-ce.

## Missão da equipe

Simule um ciclo de trabalho de um estúdio de jogos. Em duplas ou equipes, escolham uma melhoria para um modelo ou criem um jogo novo. Definam um resultado que outra pessoa consiga testar. Alternem quem programa e quem acompanha no VS Code. Outra pessoa revisa o PR antes do merge.

## 1. Prepare o ambiente e rode um modelo

Crie sua conta em [GitHub Sign up](https://github.com/signup), confirme o e-mail e entre na sua conta. Quem já tem conta pode ir direto ao botão **Fork** neste repositório. No seu fork, abra **Code → HTTPS** e copie o endereço. Substitua `SEU_USUARIO` no exemplo.

```powershell
git --version
py --version
git clone https://github.com/SEU_USUARIO/Coletanea-de-Jogos-em-Python.git
cd Coletanea-de-Jogos-em-Python
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe jogos/06_desvie.py
```

`clone` baixa o código e seu histórico, `venv` cria o ambiente isolado e `pip install -r` instala as dependências da lista. No VS Code, abra a pasta em **Arquivo → Abrir Pasta**, instale a extensão **Python** da Microsoft e selecione o interpretador da `.venv` com **Python: Select Interpreter**. Em macOS/Linux, crie a venv com `python3 -m venv .venv` e use `.venv/bin/python` nos dois últimos comandos.

## 2. Desenvolva em dupla

Crie a branch com `git switch -c oficina/minha-versao`. Copie um modelo ou comece um jogo em `contribuicoes/SEU_USUARIO/nome-do-jogo/main.py`. Registre os controles e o comando de execução em um README nessa pasta. Separe os recursos, se usados, em `assets/` dentro dela.

No VS Code, uma pessoa digita e a outra acompanha, faz perguntas e testa. Troquem os papéis depois da primeira melhoria. Para colaborar em computadores diferentes, usem [VS Code Live Share](https://learn.microsoft.com/en-us/visualstudio/liveshare/use/vscode) ou compartilhem a tela. Com Live Share, quem hospeda inicia a sessão e envia o convite à dupla. Os commits são feitos na cópia de quem hospeda.

**Exemplo de tarefa:** adicionar um som de colisão. O teste de aceitação é ouvir o som uma vez por colisão e conseguir reiniciar a rodada. Fontes para a oficina: [imagens 2D • Kenney Platformer Kit](https://kenney.nl/assets/platformer-kit) e [sons • Kenney Interface Sounds](https://kenney.nl/assets/interface-sounds). Registre a fonte e a licença de cada material usado no README do jogo.

## 3. Envie, revise e integre

```powershell
git status
git add contribuicoes/SEU_USUARIO/nome-do-jogo/
git diff --cached
git commit -m "Adiciona minha versão do jogo"
git push -u origin oficina/minha-versao
```

Confirme com `git remote -v` que `origin` aponta para seu **fork**. Se o primeiro commit pedir identidade, configure `git config user.name "Seu nome"` e `git config user.email "Seu e-mail de commit"` na pasta do repositório.

No GitHub, abra o **Pull request** com **base** `GuiPaicheco/Coletanea-de-Jogos-em-Python:main` e **compare** `SEU_USUARIO:oficina/minha-versao`. Conte o que mudou, como rodar e o que você testou. O colega revisa **Files changed**, roda o jogo e deixa feedback. Para corrigir, faça outro commit na mesma branch e use `git push`. O mantenedor demonstra o **merge** após revisão e teste. Se houver conflito, a equipe combina quais alterações preservar e volta a testar antes de integrar.

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
