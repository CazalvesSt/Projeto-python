# AstroRun

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Lucas Alves Rabelo
- João Paulo de Freitas Fadul

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.
  
## Descrição do jogo

Descreva brevemente a ideia principal do jogo.

O jogo consiste em controlar uma nave espacial que deve desviar de meteoros que surgem continuamente no topo da tela. O jogador ganha pontos a cada segundo sobrevivido e pode coletar itens de bônus para pontuação extra. A partida termina quando o jogador perde todas as vidas ao colidir com os meteoros.

## Objetivo do jogador

Explique o que o jogador precisa fazer para vencer ou avançar no jogo.

> O objetivo é sobreviver o maior tempo possível desviando dos meteoros, acumular a maior pontuação e superar o recorde salvo no jogo.

## Regras do jogo

Liste as principais regras do jogo.

- A nave se movimenta usando as setas do teclado.
- Cada segundo sobrevivido aumenta a pontuação.
- Coletar um item de bônus concede pontos extras.
- Colidir com um meteoro reduz a quantidade de vidas.
- A dificuldade aumenta a cada 15 segundos, com meteoros mais rápidos e mais frequentes.
- A partida termina quando o jogador perde todas as vidas.
  
## Controles

Informe as teclas ou comandos utilizados no jogo.

- Seta para esquerda: mover a nave para a esquerda
- Seta para direita: mover a nave para a direita
- Seta para cima: mover a nave para frente
- Seta para baixo: mover a nave para trás
- ENTER ou ESPAÇO: iniciar o jogo ou reiniciar após encerramento
- ESC: sair do jogo
  
## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```
## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.
## Observações para os alunos
- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
