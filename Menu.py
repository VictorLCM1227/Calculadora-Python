
# menu.py

from utilidades import arquivo_existe, criar_arquivo


ARQUIVO_HISTORICO = 'historico.txt'


def iniciar():

    # Verifica se o histórico existe
    if not arquivo_existe(ARQUIVO_HISTORICO):
        criar_arquivo(ARQUIVO_HISTORICO)

    # Inicia a interface
    import interface


if __name__ == '__main__':
    iniciar()