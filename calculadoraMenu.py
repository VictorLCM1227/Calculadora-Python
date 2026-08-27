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
import calculadoraUtilidades
import calculadoraFuncoes

arq = 'historico.txt'

if not calculadoraFuncoes.arquivoExiste(arq):
    calculadoraFuncoes.criarArquivo(arq)




while True:

    menu_escolha = calculadoraUtilidades.menu('CALCULADORA EM PYTHON', ['SAIR', 'SOMA', 'SUBTRAÇÃO', 'MULTIPLICAÇÃO', 'DIVISÃO', 'DIVISÃO INTEIRA', 'POTÊNCIA', 'RAIZ', 'PORCENTAGEM', 'VER HISTÓRICO', 'LIMPAR HISTÓRICO'])

    if menu_escolha == 0:
        calculadoraUtilidades.cabecalho('SAINDO...')
        break

    elif menu_escolha == 1:
        calculadoraUtilidades.cabecalho('SOMA')
        print(f'A soma deu: {calculadoraFuncoes.somar(calculadoraUtilidades.leiaFloat('Digite um número: '), calculadoraUtilidades.leiaFloat('Digite outro número para somar: ')):.3f}')

    elif menu_escolha == 2:
        calculadoraUtilidades.cabecalho('SUBTRAÇÃO')
        print(f'A subtração deu: {calculadoraFuncoes.subtrair(calculadoraUtilidades.leiaFloat('Digite um número: '), calculadoraUtilidades.leiaFloat('Digite outro número para subtrair: ')):.3f}')

    elif menu_escolha == 3:
        calculadoraUtilidades.cabecalho('MULTIPLICAÇÃO')
        print(f'A Multiplicação deu: {calculadoraFuncoes.multiplicar(calculadoraUtilidades.leiaFloat('Digite um número: '), calculadoraUtilidades.leiaFloat('Digite outro número para multiplicar: ')):.3f}')

    elif menu_escolha == 4:
        calculadoraUtilidades.cabecalho('DIVISÃO')
        print(f'A divisão deu: {calculadoraFuncoes.dividir(calculadoraUtilidades.leiaFloat('Digite um número: '), calculadoraUtilidades.leiaFloatNotZero('Digite outro número para dividir o anterior: '))}')

    elif menu_escolha == 5:
        calculadoraUtilidades.cabecalho('DIVISÃO INTEIRA')
        print(f'A divisão inteira deu: {calculadoraFuncoes.dividirInteiro(calculadoraUtilidades.leiaFloat('Digite um número: '), calculadoraUtilidades.leiaFloatNotZero('Digite outro número para dividir o anterior: '))}')

    elif menu_escolha == 6:
        calculadoraUtilidades.cabecalho('POTÊNCIA')
        print(f'A potência deu: {calculadoraFuncoes.potenciar(calculadoraUtilidades.leiaFloat('Digite um número: '), calculadoraUtilidades.leiaFloat('Digite o valor do expoente: '))}')

    elif menu_escolha == 7:
        calculadoraUtilidades.cabecalho('RAIZ')
        print(f'A raiz deu: {calculadoraFuncoes.radiciar(calculadoraUtilidades.leiaFloatPositivo('Digite um número: '), calculadoraUtilidades.leiaFloatPositivo('Digite um valor para a raiz: '))}')

    elif menu_escolha == 8:
        calculadoraUtilidades.cabecalho('PORCENTAGEM')
        print(f'O resultado é: {calculadoraFuncoes.porcentagem(calculadoraUtilidades.leiaNatural('Digite um número: '), calculadoraUtilidades.leiaFloatPositivo('Digite o valor da porcentagem: '))}')

    elif menu_escolha == 9:
        calculadoraUtilidades.cabecalho('VER HISTÓRICO')
        calculadoraFuncoes.sistema.mostrar()

    elif menu_escolha == 10:
        calculadoraUtilidades.cabecalho('LIMPAR HISTÓRICO')
        calculadoraFuncoes.sistema.limpar()
