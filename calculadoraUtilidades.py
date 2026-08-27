# CalculadoraUtilidades

from rich import print
from rich.table import Table

def linha(tamanho=30):
    return '-' * tamanho

def cabecalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())

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
            print('[red]ERRO: Por favor, digite um número maior do que zero.[/]')
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
            print('[red]ERRO: Por favor, digite um número maior ou igual a zero.[/]')
            continue

def menu(titulo, lista):
    cabecalho(titulo.upper())
    c = 0
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaNatural('Sua opção: ')
    return opc