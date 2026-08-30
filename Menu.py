# calculadoraMenu

'''
objetivo completo:
Uma aplicação desktop que permite realizar operações matemáticas básicas através de uma interface gráfica.


Etapa 3 — Interface
Criar janela
Criar display
Criar botões numéricos
Criar botões das operações
Etapa 4 — Integração
Conectar botões à lógica
Mostrar resultados
Tratar erros
Etapa 5 — Finalização
Melhorar visual
Organizar código
Adicionar README
Corrigir bugs

'''

from Utilidades import cabecalho, leiaFloat, leiaFloatNotZero, leiaFloatPositivo, leiaNatural, menu
from Funcoes import arquivoExiste, criarArquivo, dividir, dividirInteiro, multiplicar, porcentagem, potenciar, radiciar, somar, subtrair, sistema

arq = 'historico.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)




while True:

    menu_escolha = menu('CALCULADORA EM PYTHON', ['SAIR', 'SOMA', 'SUBTRAÇÃO', 'MULTIPLICAÇÃO', 'DIVISÃO', 'DIVISÃO INTEIRA', 'POTÊNCIA', 'RAIZ', 'PORCENTAGEM', 'VER HISTÓRICO', 'LIMPAR HISTÓRICO'])

    match menu_escolha:

        case 0:
            cabecalho('SAINDO...')
            break

        case 1:
            cabecalho('SOMA')
            print(f'A soma deu: {somar(leiaFloat('Digite um número: '), leiaFloat('Digite outro número para somar: ')):.3f}')

        case 2:
            cabecalho('SUBTRAÇÃO')
            print(f'A subtração deu: {subtrair(leiaFloat('Digite um número: '), leiaFloat('Digite outro número para subtrair: ')):.3f}')

        case 3:
            cabecalho('MULTIPLICAÇÃO')
            print(f'A Multiplicação deu: {multiplicar(leiaFloat('Digite um número: '), leiaFloat('Digite outro número para multiplicar: ')):.3f}')

        case 4:
            cabecalho('DIVISÃO')
            print(f'A divisão deu: {dividir(leiaFloat('Digite um número: '), leiaFloatNotZero('Digite outro número para dividir o anterior: '))}')

        case 5:
            cabecalho('DIVISÃO INTEIRA')
            print(f'A divisão inteira deu: {dividirInteiro(leiaFloat('Digite um número: '), leiaFloatNotZero('Digite outro número para dividir o anterior: '))}')

        case 6:
            cabecalho('POTÊNCIA')
            print(f'A potência deu: {potenciar(leiaFloat('Digite um número: '), leiaFloat('Digite o valor do expoente: '))}')

        case 7:
            cabecalho('RAIZ')
            print(f'A raiz deu: {radiciar(leiaFloatPositivo('Digite um número: '), leiaFloatPositivo('Digite um valor para a raiz: '))}')

        case 8:
            cabecalho('PORCENTAGEM')
            print(f'O resultado é: {porcentagem(leiaNatural('Digite um número: '),leiaFloatPositivo('Digite o valor da porcentagem: '))}')

        case 9:
            cabecalho('VER HISTÓRICO')
            sistema.mostrar()

        case 10:
            cabecalho('LIMPAR HISTÓRICO')
            sistema.limpar()

        case _:
            print("Opção inválida!")
