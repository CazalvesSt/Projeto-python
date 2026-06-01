# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

AstroRun

Exemplo:

> Corrida dos Obstáculos

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1: Lucas Alves Rabelo
- Nome 2: João Paulo de Freitas Fadul
- Nome 3:
- Nome 4:

## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo:

> Nave desviando de meteoros.

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição:

> O jogador controla uma nave espacial posicionada na parte inferior da tela. Meteoros surgem aleatoriamente no topo e descem em direção à nave. O jogador deve desviar dos meteoros movendo a nave em todas as direções. Itens de bônus aparecem esporadicamente e podem ser coletados para pontuação extra. A dificuldade aumenta com o tempo, com meteoros mais rápidos e mais frequentes.

## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

> Sobreviver pelo maior tempo possível desviando dos meteoros, acumular a maior pontuação e superar o recorde salvo no jogo.

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

- Regra 1: O jogador começa com 3 vidas.
- Regra 2: Cada segundo sobrevivido adiciona pontos ao placar.
- Regra 3: Colidir com um meteoro remove 1 vida.
- Regra 4: Coletar um item de bônus concede pontos extras.
- Regra 5: A cada 15 segundos, a velocidade e a frequência dos meteoros aumentam.

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

> Não há condição de vitória absoluta. O jogo é de sobrevivência contínua. O critério de êxito é superar o próprio recorde salvo no arquivo do jogo, o que é registrado ao final de cada partida.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

> A partida encerra quando o jogador perde as 3 vidas ao colidir com meteoros. Uma tela de Game Over é exibida com a pontuação final e o recorde anterior. Caso a pontuação atual seja maior, o arquivo de recorde é atualizado.

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

> Um personagem controlado pelas setas do teclado.

Descrição:

> Uma nave espacial controlada pelas setas do teclado, que se move nas quatro direções dentro dos limites da tela.

## Obstáculos, inimigos ou desafios

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

> Meteoros surgem continuamente no topo da tela em posições aleatórias e descem em direção à nave em velocidades e tamanhos variados.

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

> Meteoros surgem continuamente na parte superior da tela e descem em direção à nave do jogador. Itens de bônus em formato de estrela aparecem aleatoriamente durante a partida e aumentam a pontuação quando a nave passa sobre eles.

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

> O jogador começa com 3 vidas. Cada segundo sobrevivido adiciona pontos ao placar. Coletar um item de bônus concede pontos extras. Colidir com um meteoro reduz uma vida. A dificuldade aumenta a cada 15 segundos, com meteoros mais rápidos e mais frequentes.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Tecla/comando: Seta para esquerda — mover a nave para a esquerda
- Tecla/comando: Seta para direita — mover a nave para a direita
- Tecla/comando: Seta para cima — mover a nave para frente
- Tecla/comando: Seta para baixo — mover a nave para trás
- Tecla/comando: ENTER ou ESPAÇO — iniciar o jogo ou reiniciar após encerramento
- Tecla/comando: ESC — sair do jogo

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

- `main.py`: ponto de entrada do jogo, responsável por inicializar o Pygame e chamar o loop principal;
- `src/game.py`: contém o loop principal e o controle dos estados do jogo, como menu, rodando e game over;
- `src/player.py`: contém a lógica de movimentação e controle da nave do jogador;
- `src/obstacles.py`: responsável pela geração e movimentação dos meteoros;
- `src/items.py`: responsável pelos itens de bônus, incluindo geração e coleta;
- `src/utils.py`: contém funções auxiliares de lógica pura, como detecção de colisão e cálculo de pontuação;
- `src/arquivos.py`: contém as funções de leitura e escrita do arquivo de recorde;
- `src/config.py`: armazena configurações globais como dimensões da tela, cores e parâmetros de dificuldade;
- `tests/test_logica.py`: contém os testes unitários das funções de lógica do jogo.


## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

- Fonte personalizada obtida de banco gratuito para exibição do placar e das telas de menu e game over;
- Sons simples de colisão e de coleta de item obtidos de banco de áudio com licença livre;
- Tutoriais de Pygame utilizados apenas como referência para estruturação do loop principal e tratamento de eventos.

Caso não pretenda utilizar recursos externos, escreva:

> Não pretendemos utilizar recursos externos.

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1: Detecção de colisão entre a nave e múltiplos meteoros em cada frame do loop principal.
- Dificuldade 2: Controle de dificuldade progressiva de forma equilibrada, sem tornar o jogo injogável rapidamente.
- Dificuldade 3: Leitura e escrita do arquivo de recorde com tratamento correto para o caso em que o arquivo ainda não existe.

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

> A versão mínima do jogo terá uma nave controlada pelo teclado, meteoros surgindo e descendo com velocidade crescente, detecção de colisão, sistema de 3 vidas, pontuação por tempo sobrevivido, tela de Game Over e leitura e gravação do recorde em arquivo.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1: Tela inicial com título e instrução para começar.
- Melhoria 2: Sons de colisão e música de fundo.
- Melhoria 3: Item de bônus coletável com efeito visual.
