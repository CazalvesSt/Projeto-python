import os
import pytest
from src.utils import verificar_colisao, ler_recorde, salvar_recorde, calcular_pontuacao
from src.config import PONTOS_POR_SEGUNDO

ARQUIVO_TESTE = "data/recorde_teste.txt"


def setup_function():
    if os.path.exists(ARQUIVO_TESTE):
        os.remove(ARQUIVO_TESTE)


def test_colisao_detectada():
    assert verificar_colisao(0, 0, 50, 50, 25, 25, 50, 50) is True


def test_sem_colisao_horizontal():
    assert verificar_colisao(0, 0, 50, 50, 100, 0, 50, 50) is False


def test_sem_colisao_vertical():
    assert verificar_colisao(0, 0, 50, 50, 0, 100, 50, 50) is False


def test_colisao_na_borda():
    assert verificar_colisao(0, 0, 50, 50, 50, 0, 50, 50) is False


def test_pontuacao_incrementa():
    assert calcular_pontuacao(5, PONTOS_POR_SEGUNDO) == 5 * PONTOS_POR_SEGUNDO


def test_pontuacao_zero():
    assert calcular_pontuacao(0, PONTOS_POR_SEGUNDO) == 0


def test_leitura_recorde_arquivo_inexistente(monkeypatch):
    monkeypatch.setattr("src.utils.ARQUIVO_RECORDE", ARQUIVO_TESTE)
    assert ler_recorde() == 0


def test_gravacao_e_leitura_recorde(monkeypatch):
    monkeypatch.setattr("src.utils.ARQUIVO_RECORDE", ARQUIVO_TESTE)
    salvar_recorde(500)
    assert ler_recorde() == 500


def test_recorde_atualizado_quando_maior(monkeypatch):
    monkeypatch.setattr("src.utils.ARQUIVO_RECORDE", ARQUIVO_TESTE)
    salvar_recorde(300)
    resultado = salvar_recorde(700)
    assert resultado is True
    assert ler_recorde() == 700


def test_recorde_nao_atualizado_quando_menor(monkeypatch):
    monkeypatch.setattr("src.utils.ARQUIVO_RECORDE", ARQUIVO_TESTE)
    salvar_recorde(800)
    resultado = salvar_recorde(200)
    assert resultado is False
    assert ler_recorde() == 800
