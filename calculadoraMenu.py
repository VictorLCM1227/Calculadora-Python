# calculadoraMenu

'''
1. objetivo completo:
Uma aplicação desktop que permite realizar operações matemáticas básicas através de uma interface gráfica.

2. funcionalidades:
somar
multiplicar
subtrair
dividir
divisao inteira
limpar o resultado
histórico salvo em txt
porcentagem
raiz
potência
limpar historico

Etapa 1 — Estrutura
Criar a pasta do projeto
Criar os módulos
Definir as dependências

Etapa 2 — Lógica
Criar função de soma
Criar função de subtração
Criar função de multiplicação
Criar função de divisão
Testar todas
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

menu_escolha = calculadoraUtilidades.menu('CALCULADORA EM PYTHON', ['SAIR', 'SOMA', 'SUBTRAÇÃO', 'MULTIPLICAÇÃO', 'DIVISÃO', 'DIVISÃO INTEIRA', 'POTÊNCIA', 'RAIZ', 'PORCENTAGAM', 'VER HISTÓRICO', 'LIMPAR HISTÓRICO'])

if menu_escolha == 0:
    calculadoraUtilidades.cabecalho('SAINDO...')

elif menu_escolha == 1:
    calculadoraUtilidades.cabecalho('SOMA')
    print(f'A soma deu: {calculadoraFuncoes.somar(calculadoraUtilidades.leiaFloat('Digite um número: '), calculadoraUtilidades.leiaFloat('Digite outro número para somar: ')):.3f}')

elif menu_escolha == 2:
    calculadoraUtilidades.cabecalho('SUBTRAÇÃO')
    print(f'A subtração deu: {calculadoraFuncoes.subtrair(calculadoraUtilidades.leiaFloat('Digite um número: '), calculadoraUtilidades.leiaFloat('Digite outro número para subtrair: ')):.3f}')

    
# repetir a lógica para as outras operações