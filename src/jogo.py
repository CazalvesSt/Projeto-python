import pygame
import sys
from src.config import (
    LARGURA, ALTURA, FPS, TITULO,
    AZUL_ESCURO, BRANCO, CINZA, CIANO, AMARELO, VERMELHO,
    JOGADOR_VIDAS, METEORO_VEL_INICIAL, METEORO_INTERVALO,
    BONUS_INTERVALO, BONUS_PONTOS, PONTOS_POR_SEGUNDO,
    DIFICULDADE_INTERVALO
)
from src.player    import Jogador
from src.obstacles import criar_meteoro, atualizar_meteoros, desenhar_meteoros
from src.items     import criar_bonus, atualizar_bonus, desenhar_bonus
from src.utils     import verificar_colisao, ler_recorde, salvar_recorde


ESTADO_MENU     = "menu"
ESTADO_JOGANDO  = "jogando"
ESTADO_GAMEOVER = "gameover"


def inicializar_pygame():
    """Inicializa o Pygame e cria a janela."""
    pygame.init()
    tela  = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption(TITULO)
    clock = pygame.time.Clock()
    return tela, clock


def obter_fontes():
    """Carrega as fontes utilizadas nas telas."""
    fonte_titulo  = pygame.font.SysFont("arial", 52, bold=True)
    fonte_grande  = pygame.font.SysFont("arial", 36, bold=True)
    fonte_media   = pygame.font.SysFont("arial", 26)
    fonte_pequena = pygame.font.SysFont("arial", 20)
    return fonte_titulo, fonte_grande, fonte_media, fonte_pequena


def resetar_estado_jogo():
    """Retorna um dicionario com o estado inicial de uma nova partida."""
    return {
        "jogador":          Jogador(),
        "vidas":            JOGADOR_VIDAS,
        "pontuacao":        0,
        "tempo_frames":     0,
        "vel_meteoro":      METEORO_VEL_INICIAL,
        "intervalo_meteor": METEORO_INTERVALO,
        "contador_meteor":  0,
        "contador_bonus":   0,
        "lista_meteoros":   [],
        "lista_bonus":      [],
        "novo_recorde":     False,
    }


def desenhar_fundo(tela):
    tela.fill(AZUL_ESCURO)


def desenhar_hud(tela, estado, fonte_media, fonte_pequena, recorde):
    """Desenha pontuacao, vidas e recorde na tela durante o jogo."""
    segundos  = estado["tempo_frames"] // FPS
    pontuacao = segundos * PONTOS_POR_SEGUNDO + estado["pontuacao"]

    txt_pts = fonte_media.render(f"Pontos: {pontuacao}", True, BRANCO)
    txt_rec = fonte_pequena.render(f"Recorde: {recorde}", True, CINZA)
    txt_vid = fonte_media.render(f"Vidas: {estado['vidas']}", True, CIANO)

    tela.blit(txt_pts, (10, 10))
    tela.blit(txt_rec, (10, 40))
    tela.blit(txt_vid, (LARGURA - txt_vid.get_width() - 10, 10))


def desenhar_tela_menu(tela, fontes, recorde):
    fonte_titulo, fonte_grande, fonte_media, fonte_pequena = fontes
    desenhar_fundo(tela)

    titulo = fonte_titulo.render("ASTRORUN", True, CIANO)
    sub    = fonte_media.render("Desvie dos meteoros e sobreviva!", True, BRANCO)
    rec    = fonte_pequena.render(f"Recorde atual: {recorde}", True, AMARELO)
    ini    = fonte_grande.render("Pressione ENTER para jogar", True, BRANCO)

    tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 160))
    tela.blit(sub,    (LARGURA // 2 - sub.get_width()    // 2, 240))
    tela.blit(rec,    (LARGURA // 2 - rec.get_width()    // 2, 290))
    tela.blit(ini,    (LARGURA // 2 - ini.get_width()    // 2, 380))


def desenhar_tela_gameover(tela, fontes, estado, recorde):
    fonte_titulo, fonte_grande, fonte_media, fonte_pequena = fontes
    desenhar_fundo(tela)

    segundos  = estado["tempo_frames"] // FPS
    pontuacao = segundos * PONTOS_POR_SEGUNDO + estado["pontuacao"]

    txt_go  = fonte_titulo.render("GAME OVER", True, VERMELHO)
    txt_pts = fonte_grande.render(f"Pontuacao: {pontuacao}", True, BRANCO)
    txt_rec = fonte_media.render(f"Recorde: {recorde}", True, AMARELO)
    txt_ini = fonte_media.render("Pressione ENTER para jogar novamente", True, CINZA)
    txt_esc = fonte_pequena.render("ESC para sair", True, CINZA)

    tela.blit(txt_go,  (LARGURA // 2 - txt_go.get_width()  // 2, 150))
    tela.blit(txt_pts, (LARGURA // 2 - txt_pts.get_width() // 2, 240))
    tela.blit(txt_rec, (LARGURA // 2 - txt_rec.get_width() // 2, 290))

    if estado["novo_recorde"]:
        txt_nr = fonte_media.render("Novo recorde!", True, AMARELO)
        tela.blit(txt_nr, (LARGURA // 2 - txt_nr.get_width() // 2, 340))

    tela.blit(txt_ini, (LARGURA // 2 - txt_ini.get_width() // 2, 420))
    tela.blit(txt_esc, (LARGURA // 2 - txt_esc.get_width() // 2, 460))


def atualizar_jogo(estado):
    """
    Executa um frame da logica do jogo.
    Retorna True se o jogador ainda esta vivo, False se perdeu todas as vidas.
    """
    jogador = estado["jogador"]
    teclas  = pygame.key.get_pressed()

    jogador.mover(teclas)
    jogador.atualizar()

    estado["tempo_frames"]    += 1
    estado["contador_meteor"] += 1
    estado["contador_bonus"]  += 1

    segundos = estado["tempo_frames"] // FPS
    if segundos > 0 and segundos % DIFICULDADE_INTERVALO == 0 and estado["tempo_frames"] % FPS == 0:
        estado["vel_meteoro"]      += 0.5
        estado["intervalo_meteor"] = max(20, estado["intervalo_meteor"] - 5)

    if estado["contador_meteor"] >= estado["intervalo_meteor"]:
        estado["lista_meteoros"].append(criar_meteoro(estado["vel_meteoro"]))
        estado["contador_meteor"] = 0

    if estado["contador_bonus"] >= BONUS_INTERVALO:
        estado["lista_bonus"].append(criar_bonus())
        estado["contador_bonus"] = 0

    atualizar_meteoros(estado["lista_meteoros"])
    atualizar_bonus(estado["lista_bonus"])

    jx, jy, jw, jh = jogador.rect
    for meteoro in estado["lista_meteoros"][:]:
        if verificar_colisao(jx, jy, jw, jh,
                             meteoro["x"], meteoro["y"],
                             meteoro["largura"], meteoro["altura"]):
            if jogador.sofrer_dano():
                estado["vidas"] -= 1
                estado["lista_meteoros"].remove(meteoro)
                if estado["vidas"] <= 0:
                    return False

    for bonus in estado["lista_bonus"][:]:
        if verificar_colisao(jx, jy, jw, jh,
                             bonus["x"], bonus["y"],
                             bonus["largura"], bonus["altura"]):
            estado["pontuacao"]  += BONUS_PONTOS
            estado["lista_bonus"].remove(bonus)

    return True


def executar_jogo():
    """Funcao principal chamada pelo main.py."""
    tela, clock = inicializar_pygame()
    fontes      = obter_fontes()
    recorde     = ler_recorde()
    estado_tela = ESTADO_MENU
    estado      = resetar_estado_jogo()

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    if estado_tela in (ESTADO_MENU, ESTADO_GAMEOVER):
                        estado      = resetar_estado_jogo()
                        estado_tela = ESTADO_JOGANDO

        if estado_tela == ESTADO_MENU:
            desenhar_tela_menu(tela, fontes, recorde)

        elif estado_tela == ESTADO_JOGANDO:
            vivo = atualizar_jogo(estado)
            desenhar_fundo(tela)
            desenhar_meteoros(tela, estado["lista_meteoros"])
            desenhar_bonus(tela,    estado["lista_bonus"])
            estado["jogador"].desenhar(tela)
            desenhar_hud(tela, estado, fontes[2], fontes[3], recorde)

            if not vivo:
                segundos  = estado["tempo_frames"] // FPS
                pontuacao = segundos * PONTOS_POR_SEGUNDO + estado["pontuacao"]
                novo      = salvar_recorde(pontuacao)
                recorde   = ler_recorde()
                estado["novo_recorde"] = novo
                estado_tela = ESTADO_GAMEOVER

        elif estado_tela == ESTADO_GAMEOVER:
            desenhar_tela_gameover(tela, fontes, estado, recorde)

        pygame.display.flip()
