# utilidades.py

import os


def arquivo_existe(nome):
    """
    Verifica se um arquivo existe.
    """

    return os.path.exists(nome)


def criar_arquivo(nome):
    """
    Cria um arquivo caso ele não exista.
    """

    try:
        with open(nome, 'a', encoding='utf-8'):
            pass

    except OSError as erro:
        print(f'Erro ao criar o arquivo: {erro}')


def formatar_resultado(resultado):
    """
    Formata o resultado para evitar mostrar .0
    quando o número é inteiro.
    """

    if resultado == int(resultado):
        return str(int(resultado))

    return str(resultado)
