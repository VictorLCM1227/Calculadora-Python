'''
┌─────────────────────────┐
│                   123   │
├─────┬─────┬─────┬───────┤
│  7  │  8  │  9  │   ÷   │
├─────┼─────┼─────┼───────┤
│  4  │  5  │  6  │   ×   │
├─────┼─────┼─────┼───────┤
│  1  │  2  │  3  │   −   │
├─────┼─────┼─────┼───────┤
│  0  │  C  │  =  │   +   │
└─────┴─────┴─────┴───────┘
'''

# criar a janela principal

import tkinter as tk
from tkinter import ttk, messagebox

janela = tk.Tk()

janela.title('CALCULADORA')
janela.geometry('350x500+20+20')

# Variável que controla o conteúdo do display
valor_display = tk.StringVar(value='0')

# Display
txt_display = ttk.Entry(
    janela,
    textvariable=valor_display,
    font=("Arial", 16, "bold"),
    justify='right',
    state='disabled'
)

# Botões
btn_7 = ttk.Button(janela, text='7')
btn_8 = ttk.Button(janela, text='8')
btn_9 = ttk.Button(janela, text='9')
btn_dividir = ttk.Button(janela, text='÷')

btn_4 = ttk.Button(janela, text='4')
btn_5 = ttk.Button(janela, text='5')
btn_6 = ttk.Button(janela, text='6')
btn_x = ttk.Button(janela, text='x')

btn_1 = ttk.Button(janela, text='1')
btn_2 = ttk.Button(janela, text='2')
btn_3 = ttk.Button(janela, text='3')
btn_menos = ttk.Button(janela, text='-')

btn_0 = ttk.Button(janela, text='0')
btn_c = ttk.Button(janela, text='C')
btn_igual = ttk.Button(janela, text='=')
btn_mais = ttk.Button(janela, text='+')

# Display
txt_display.grid(row=0, column=0, columnspan=4)

# Primeira linha
btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_dividir.grid(row=1, column=3)

# Segunda linha
btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_x.grid(row=2, column=3)

# Terceira linha
btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_menos.grid(row=3, column=3)

# Quarta linha
btn_0.grid(row=4, column=0)
btn_c.grid(row=4, column=1)
btn_igual.grid(row=4, column=2)
btn_mais.grid(row=4, column=3)

janela.mainloop()