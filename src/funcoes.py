import random
from src.config import (
    LARGURA, METEORO_LARGURA_MIN, METEORO_LARGURA_MAX,
    BONUS_LARGURA, BONUS_VEL, PONTOS_POR_SEGUNDO
)


def verificar_colisao(ax, ay, aw, ah, bx, by, bw, bh):
    """
    Verifica colisao entre dois retangulos.
    Retorna True se houver sobreposicao, False caso contrario.
    """
    return (
        ax < bx + bw and
        ax + aw > bx and
        ay < by + bh and
        ay + ah > by
    )


def calcular_pontuacao(segundos_sobrevividos):
    """Calcula a pontuacao baseada no tempo sobrevivido."""
    return segundos_sobrevividos * PONTOS_POR_SEGUNDO


def criar_meteoro(velocidade):
    """
    Cria um novo meteoro com posicao e tamanho aleatorios.
    Retorna um dicionario com os dados do meteoro.
    """
    largura = random.randint(METEORO_LARGURA_MIN, METEORO_LARGURA_MAX)
    altura  = random.randint(METEORO_LARGURA_MIN, METEORO_LARGURA_MAX)
    x       = random.randint(0, LARGURA - largura)
    return {
        "x":       x,
        "y":       -altura,
        "largura": largura,
        "altura":  altura,
        "vel":     velocidade + random.uniform(-0.5, 1.0)
    }


def atualizar_meteoros(lista_meteoros):
    """Move todos os meteoros para baixo e remove os que saem da tela."""
    for m in lista_meteoros:
        m["y"] += m["vel"]
    lista_meteoros[:] = [m for m in lista_meteoros if m["y"] < 620]


def criar_bonus():
    """Cria um item de bonus em posicao aleatoria no topo da tela."""
    x = random.randint(0, LARGURA - BONUS_LARGURA)
    return {
        "x":       x,
        "y":       -BONUS_LARGURA,
        "largura": BONUS_LARGURA,
        "altura":  BONUS_LARGURA,
        "vel":     BONUS_VEL
    }


def atualizar_bonus(lista_bonus):
    """Move os itens de bonus e remove os que saem da tela."""
    for b in lista_bonus:
        b["y"] += b["vel"]
    lista_bonus[:] = [b for b in lista_bonus if b["y"] < 620]


def mover_jogador(jogador, teclas):
    """Movimenta a nave com base nas teclas pressionadas."""
    import pygame
    from src.config import JOGADOR_VEL, LARGURA, ALTURA, JOGADOR_LARGURA, JOGADOR_ALTURA

    if teclas[pygame.K_LEFT] and jogador["x"] > 0:
        jogador["x"] -= JOGADOR_VEL
    if teclas[pygame.K_RIGHT] and jogador["x"] + JOGADOR_LARGURA < LARGURA:
        jogador["x"] += JOGADOR_VEL
    if teclas[pygame.K_UP] and jogador["y"] > 0:
        jogador["y"] -= JOGADOR_VEL
    if teclas[pygame.K_DOWN] and jogador["y"] + JOGADOR_ALTURA < ALTURA:
        jogador["y"] += JOGADOR_VEL


def atualizar_invulnerabilidade(jogador):
    """Atualiza o contador de invulnerabilidade do jogador."""
    if jogador["invulneravel"]:
        jogador["tempo_invuln"] += 1
        if jogador["tempo_invuln"] >= jogador["duracao_invuln"]:
            jogador["invulneravel"] = False
            jogador["tempo_invuln"] = 0


def sofrer_dano(jogador):
    """
    Aplica dano ao jogador se nao estiver invulneravel.
    Retorna True se o dano foi aplicado.
    """
    if not jogador["invulneravel"]:
        jogador["invulneravel"] = True
        jogador["tempo_invuln"] = 0
        return True
    return False


def criar_jogador():
    """Retorna o dicionario de estado inicial do jogador."""
    from src.config import LARGURA, ALTURA, JOGADOR_LARGURA, JOGADOR_ALTURA
    return {
        "x":            LARGURA // 2 - JOGADOR_LARGURA // 2,
        "y":            ALTURA - JOGADOR_ALTURA - 20,
        "invulneravel": False,
        "tempo_invuln": 0,
        "duracao_invuln": 90
    }
