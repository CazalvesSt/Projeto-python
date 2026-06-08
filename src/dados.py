import os
from src.config import ARQUIVO_RECORDE


def ler_recorde():
    """
    Le o recorde salvo em arquivo.
    Retorna 0 se o arquivo nao existir ou estiver corrompido.
    """
    try:
        with open(ARQUIVO_RECORDE, "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def salvar_recorde(pontuacao):
    """
    Salva a pontuacao como novo recorde, somente se for maior que o atual.
    Retorna True se o recorde foi atualizado, False caso contrario.
    """
    recorde_atual = ler_recorde()
    if pontuacao > recorde_atual:
        os.makedirs(os.path.dirname(ARQUIVO_RECORDE), exist_ok=True)
        with open(ARQUIVO_RECORDE, "w") as f:
            f.write(str(pontuacao))
        return True
    return False
