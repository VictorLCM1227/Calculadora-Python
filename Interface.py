
# interface.py

import tkinter as tk
from tkinter import ttk, messagebox

from funcoes import (
    somar,
    subtrair,
    multiplicar,
    dividir
)

from funcoes import sistema


# ============================================================
# JANELA
# ============================================================

janela = tk.Tk()

janela.title('Calculadora')
janela.geometry('350x500')
janela.resizable(False, False)


# ============================================================
# VARIÁVEIS
# ============================================================

valor_display = tk.StringVar(value='0')

numero_atual = ''

primeiro_numero = None

operacao = None


# ============================================================
# FUNÇÕES DA INTERFACE
# ============================================================

def adicionar_numero(numero):
    """
    Adiciona um número ao display.
    """

    global numero_atual

    if numero_atual == '0':
        numero_atual = ''

    numero_atual += str(numero)

    valor_display.set(numero_atual)


def limpar():
    """
    Limpa a calculadora.
    """

    global numero_atual
    global primeiro_numero
    global operacao

    numero_atual = ''
    primeiro_numero = None
    operacao = None

    valor_display.set('0')


def escolher_operacao(op):
    """
    Armazena o primeiro número e a operação escolhida.
    """

    global numero_atual
    global primeiro_numero
    global operacao

    if numero_atual == '':
        return

    primeiro_numero = float(numero_atual)

    operacao = op

    numero_atual = ''

    valor_display.set('0')


def calcular():
    """
    Realiza a operação escolhida.
    """

    global numero_atual
    global primeiro_numero
    global operacao

    if primeiro_numero is None:
        return

    if numero_atual == '':
        return

    segundo_numero = float(numero_atual)

    try:

        if operacao == '+':

            resultado = somar(
                primeiro_numero,
                segundo_numero
            )

        elif operacao == '-':

            resultado = subtrair(
                primeiro_numero,
                segundo_numero
            )

        elif operacao == '*':

            resultado = multiplicar(
                primeiro_numero,
                segundo_numero
            )

        elif operacao == '/':

            resultado = dividir(
                primeiro_numero,
                segundo_numero
            )

        else:
            return


        # Remove .0 de resultados inteiros
        if resultado == int(resultado):
            resultado = int(resultado)


        valor_display.set(str(resultado))

        numero_atual = str(resultado)

        primeiro_numero = None

        operacao = None


    except ZeroDivisionError:

        messagebox.showerror(
            'Erro',
            'Não é possível dividir por zero.'
        )

        limpar()


def mostrar_historico():
    """
    Abre uma janela com o histórico das operações.
    """

    historico = sistema.mostrar()


    janela_historico = tk.Toplevel(janela)

    janela_historico.title('Histórico')

    janela_historico.geometry('350x400')

    janela_historico.resizable(False, False)


    # Título
    titulo = ttk.Label(
        janela_historico,
        text='HISTÓRICO',
        font=('Arial', 18, 'bold')
    )

    titulo.pack(pady=10)


    # Área de texto
    texto = tk.Text(
        janela_historico,
        font=('Arial', 12),
        state='normal'
    )

    texto.pack(
        fill='both',
        expand=True,
        padx=10,
        pady=10
    )


    texto.insert(
        '1.0',
        historico
    )


    texto.config(
        state='disabled'
    )


    # Botão limpar
    def limpar_historico():

        sistema.limpar()

        texto.config(state='normal')

        texto.delete(
            '1.0',
            tk.END
        )

        texto.insert(
            '1.0',
            'O histórico está vazio.'
        )

        texto.config(state='disabled')


    btn_limpar = ttk.Button(
        janela_historico,
        text='Limpar histórico',
        command=limpar_historico
    )

    btn_limpar.pack(
        pady=10
    )


# ============================================================
# DISPLAY
# ============================================================

txt_display = ttk.Entry(
    janela,
    textvariable=valor_display,
    font=('Arial', 24, 'bold'),
    justify='right',
    state='readonly'
)

txt_display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=15,
    sticky='nsew',
    ipady=15
)


# ============================================================
# BOTÕES
# ============================================================

btn_7 = ttk.Button(
    janela,
    text='7',
    command=lambda: adicionar_numero(7)
)

btn_8 = ttk.Button(
    janela,
    text='8',
    command=lambda: adicionar_numero(8)
)

btn_9 = ttk.Button(
    janela,
    text='9',
    command=lambda: adicionar_numero(9)
)

btn_dividir = ttk.Button(
    janela,
    text='÷',
    command=lambda: escolher_operacao('/')
)


btn_4 = ttk.Button(
    janela,
    text='4',
    command=lambda: adicionar_numero(4)
)

btn_5 = ttk.Button(
    janela,
    text='5',
    command=lambda: adicionar_numero(5)
)

btn_6 = ttk.Button(
    janela,
    text='6',
    command=lambda: adicionar_numero(6)
)

btn_multiplicar = ttk.Button(
    janela,
    text='×',
    command=lambda: escolher_operacao('*')
)


btn_1 = ttk.Button(
    janela,
    text='1',
    command=lambda: adicionar_numero(1)
)

btn_2 = ttk.Button(
    janela,
    text='2',
    command=lambda: adicionar_numero(2)
)

btn_3 = ttk.Button(
    janela,
    text='3',
    command=lambda: adicionar_numero(3)
)

btn_subtrair = ttk.Button(
    janela,
    text='−',
    command=lambda: escolher_operacao('-')
)


btn_0 = ttk.Button(
    janela,
    text='0',
    command=lambda: adicionar_numero(0)
)

btn_limpar = ttk.Button(
    janela,
    text='C',
    command=limpar
)

btn_igual = ttk.Button(
    janela,
    text='=',
    command=calcular
)

btn_somar = ttk.Button(
    janela,
    text='+',
    command=lambda: escolher_operacao('+')
)


# ============================================================
# POSICIONAMENTO
# ============================================================

# 7 8 9 ÷
btn_7.grid(
    row=1,
    column=0,
    padx=5,
    pady=5,
    sticky='nsew'
)

btn_8.grid(
    row=1,
    column=1,
    padx=5,
    pady=5,
    sticky='nsew'
)

btn_9.grid(
    row=1,
    column=2,
    padx=5,
    pady=5,
    sticky='nsew'
)

btn_dividir.grid(
    row=1,
    column=3,
    padx=5,
    pady=5,
    sticky='nsew'
)


# 4 5 6 ×
btn_4.grid(
    row=2,
    column=0,
    padx=5,
    pady=5,
    sticky='nsew'
)

btn_5.grid(
    row=2,
    column=1,
    padx=5,
    pady=5,
    sticky='nsew'
)

btn_6.grid(
    row=2,
    column=2,
    padx=5,
    pady=5,
    sticky='nsew'
)

btn_multiplicar.grid(
    row=2,
    column=3,
    padx=5,
    pady=5,
    sticky='nsew'
)


# 1 2 3 -
btn_1.grid(
    row=3,
    column=0,
    padx=5,
    pady=5,
    sticky='nsew'
)

btn_2.grid(
    row=3,
    column=1,
    padx=5,
    pady=5,
    sticky='nsew'
)

btn_3.grid(
    row=3,
    column=2,
    padx=5,
    pady=5,
    sticky='nsew'
)

btn_subtrair.grid(
    row=3,
    column=3,
    padx=5,
    pady=5,
    sticky='nsew'
)


# 0 C = +
btn_0.grid(
    row=4,
    column=0,
    padx=5,
    pady=5,
    sticky='nsew'
)

btn_limpar.grid(
    row=4,
    column=1,
    padx=5,
    pady=5,
    sticky='nsew'
)

btn_igual.grid(
    row=4,
    column=2,
    padx=5,
    pady=5,
    sticky='nsew'
)

btn_somar.grid(
    row=4,
    column=3,
    padx=5,
    pady=5,
    sticky='nsew'
)


# ============================================================
# HISTÓRICO
# ============================================================

btn_historico = ttk.Button(
    janela,
    text='Histórico',
    command=mostrar_historico
)

btn_historico.grid(
    row=5,
    column=0,
    columnspan=4,
    padx=5,
    pady=10,
    sticky='nsew'
)


# ============================================================
# CONFIGURAÇÃO DO GRID
# ============================================================

for coluna in range(4):

    janela.columnconfigure(
        coluna,
        weight=1
    )


for linha in range(6):

    janela.rowconfigure(
        linha,
        weight=1
    )


# ============================================================
# INICIAR INTERFACE
# ============================================================

janela.mainloop()