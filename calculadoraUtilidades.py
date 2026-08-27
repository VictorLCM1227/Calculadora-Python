from rich import print
from rich.table import Table

def linha(tamanho=30):
    return '-' * tamanho

def cabecalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())

def menu(lista):
    cabecalho

def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('[red]ERRO: Por favor, digite um número inteiro válido.[/]')
            continue
        except KeyboardInterrupt:
            print('[red]Usuário preferiu não digitar esse número.[/]')
            return 0
        else:
            return numero


def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            print('[red]ERRO: Por favor, digite um número real válido.[/]')
            continue
        except KeyboardInterrupt:
            print('[red]Usuário preferiu não digitar esse número.[/]')
            return 0
        else:
            return numero

def leiaFloatPositivo(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            print('[red]ERRO: Por favor, digite um número real válido.[/]')
            continue
        except KeyboardInterrupt:
            print('[red]Usuário preferiu não digitar esse número.[/]')
            return 0
        else:
            if numero > 0:
                return numero
            print('[red]ERRO: Por favor, digite um número maior do que zero.')
            continue

def leiaNatural(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            print('[red]ERRO: Por favor, digite um número real válido.[/]')
            continue
        except KeyboardInterrupt:
            print('[red]Usuário preferiu não digitar esse número.[/]')
            return 0
        else:
            if numero >= 0:
                return numero
            print('[red]ERRO: Por favor, digite um número maior ou igual a zero.')
            continue