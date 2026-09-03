# funcoes.py

import os

from utilidades import criar_arquivo


# ============================================================
# HISTÓRICO
# ============================================================

class HistoricoOperacoes:

    def __init__(self, nome='historico.txt'):
        self.arq = nome

        # Garante que o arquivo exista
        criar_arquivo(self.arq)


    def adicionar(self, numero1, numero2, operacao, resultado):
        """
        Adiciona uma operação ao histórico.
        """

        try:

            with open(self.arq, 'a', encoding='utf-8') as arquivo:

                arquivo.write(
                    f'{numero1} {operacao} {numero2} = {resultado}\n'
                )

        except OSError as erro:

            print(f'Erro ao salvar no histórico: {erro}')


    def mostrar(self):
        """
        Retorna todo o conteúdo do histórico.
        """

        try:

            with open(self.arq, 'r', encoding='utf-8') as arquivo:

                historico = arquivo.read()

                if historico == '':
                    return 'O histórico está vazio.'

                return historico

        except FileNotFoundError:

            return 'O histórico está vazio.'


    def limpar(self):
        """
        Limpa o histórico.
        """

        try:

            with open(self.arq, 'w', encoding='utf-8') as arquivo:
                pass

            return True

        except OSError as erro:

            print(f'Erro ao limpar histórico: {erro}')
            return False


# Objeto responsável pelo histórico
sistema = HistoricoOperacoes()


# ============================================================
# OPERAÇÕES MATEMÁTICAS
# ============================================================

def somar(numero1, numero2):

    resultado = numero1 + numero2

    sistema.adicionar(
        numero1,
        numero2,
        '+',
        resultado
    )

    return resultado


def subtrair(numero1, numero2):

    resultado = numero1 - numero2

    sistema.adicionar(
        numero1,
        numero2,
        '-',
        resultado
    )

    return resultado


def multiplicar(numero1, numero2):

    resultado = numero1 * numero2

    sistema.adicionar(
        numero1,
        numero2,
        '×',
        resultado
    )

    return resultado


def dividir(numero1, numero2):

    if numero2 == 0:
        raise ZeroDivisionError

    resultado = numero1 / numero2

    sistema.adicionar(
        numero1,
        numero2,
        '÷',
        resultado
    )

    return resultado