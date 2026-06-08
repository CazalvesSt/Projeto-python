import pygame
from src.config import (
    CIANO, BRANCO, AMARELO, LARANJA, VERMELHO,
    JOGADOR_LARGURA, JOGADOR_ALTURA
)


def desenhar_jogador(tela, jogador):
    """Desenha a nave na tela. Pisca quando invulneravel."""
    if jogador["invulneravel"] and (jogador["tempo_invuln"] // 6) % 2 == 0:
        return

    x = jogador["x"]
    y = jogador["y"]

    # Corpo da nave
    pygame.draw.rect(tela, CIANO, (x, y, JOGADOR_LARGURA, JOGADOR_ALTURA))
    # Cabine
    pygame.draw.rect(tela, BRANCO, (x + JOGADOR_LARGURA // 2 - 6, y + 4, 12, 10))
    # Chama do motor
    pygame.draw.rect(tela, AMARELO, (x + JOGADOR_LARGURA // 2 - 8, y + JOGADOR_ALTURA, 16, 6))


def desenhar_meteoros(tela, lista_meteoros):
    """Desenha todos os meteoros na tela."""
    for m in lista_meteoros:
        pygame.draw.ellipse(tela, LARANJA, (m["x"], m["y"], m["largura"], m["altura"]))
        pygame.draw.ellipse(tela, VERMELHO, (m["x"], m["y"], m["largura"], m["altura"]), 2)


def desenhar_bonus(tela, lista_bonus):
    """Desenha os itens de bonus como circulos amarelos."""
    for b in lista_bonus:
        cx = b["x"] + b["largura"] // 2
        cy = b["y"] + b["altura"] // 2
        r  = b["largura"] // 2
        pygame.draw.circle(tela, AMARELO, (cx, cy), r)
        pygame.draw.circle(tela, BRANCO,  (cx, cy), r, 2)


def desenhar_fundo(tela, cor):
    """Preenche o fundo da tela."""
    tela.fill(cor)


def desenhar_hud(tela, pontuacao, vidas, recorde, fontes):
    """Desenha pontuacao, vidas e recorde durante o jogo."""
    from src.config import LARGURA, BRANCO, CINZA, CIANO
    fonte_media, fonte_pequena = fontes

    txt_pts = fonte_media.render(f"Pontos: {pontuacao}", True, BRANCO)
    txt_rec = fonte_pequena.render(f"Recorde: {recorde}", True, CINZA)
    txt_vid = fonte_media.render(f"Vidas: {vidas}", True, CIANO)

    tela.blit(txt_pts, (10, 10))
    tela.blit(txt_rec, (10, 40))
    tela.blit(txt_vid, (LARGURA - txt_vid.get_width() - 10, 10))


def desenhar_tela_menu(tela, fontes, recorde):
    """Desenha a tela inicial do jogo."""
    from src.config import LARGURA, AZUL_ESCURO, CIANO, BRANCO, AMARELO
    fonte_titulo, fonte_grande, fonte_media, fonte_pequena = fontes

    tela.fill(AZUL_ESCURO)

    titulo = fonte_titulo.render("ASTRORUN", True, CIANO)
    sub    = fonte_media.render("Desvie dos meteoros e sobreviva!", True, BRANCO)
    rec    = fonte_pequena.render(f"Recorde atual: {recorde}", True, AMARELO)
    ini    = fonte_grande.render("Pressione ENTER para jogar", True, BRANCO)

    tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 160))
    tela.blit(sub,    (LARGURA // 2 - sub.get_width()    // 2, 240))
    tela.blit(rec,    (LARGURA // 2 - rec.get_width()    // 2, 290))
    tela.blit(ini,    (LARGURA // 2 - ini.get_width()    // 2, 380))


def desenhar_tela_gameover(tela, fontes, pontuacao, recorde, novo_recorde):
    """Desenha a tela de game over."""
    from src.config import LARGURA, AZUL_ESCURO, VERMELHO, BRANCO, AMARELO, CINZA
    fonte_titulo, fonte_grande, fonte_media, fonte_pequena = fontes

    tela.fill(AZUL_ESCURO)

    txt_go  = fonte_titulo.render("GAME OVER", True, VERMELHO)
    txt_pts = fonte_grande.render(f"Pontuacao: {pontuacao}", True, BRANCO)
    txt_rec = fonte_media.render(f"Recorde: {recorde}", True, AMARELO)
    txt_ini = fonte_media.render("Pressione ENTER para jogar novamente", True, CINZA)
    txt_esc = fonte_pequena.render("ESC para sair", True, CINZA)

    tela.blit(txt_go,  (LARGURA // 2 - txt_go.get_width()  // 2, 150))
    tela.blit(txt_pts, (LARGURA // 2 - txt_pts.get_width() // 2, 240))
    tela.blit(txt_rec, (LARGURA // 2 - txt_rec.get_width() // 2, 290))

    if novo_recorde:
        txt_nr = fonte_media.render("Novo recorde!", True, AMARELO)
        tela.blit(txt_nr, (LARGURA // 2 - txt_nr.get_width() // 2, 340))

    tela.blit(txt_ini, (LARGURA // 2 - txt_ini.get_width() // 2, 420))
    tela.blit(txt_esc, (LARGURA // 2 - txt_esc.get_width() // 2, 460))
