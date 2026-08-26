from rich import print
from rich.table import Table

def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('[red]ERRO: Por favor, digite um número inteiro válido.[/]')
            continue
        except KeyboardInterrupt:
            print('[red]Usuário preferiu não digitar esse número.')
            return 0
        else:
            return numero

def linha(tamanho=30):
    return '-' * tamanho

def cabecalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())

def menu(lista)
    cabecalho