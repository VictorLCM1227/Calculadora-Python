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

#criar a janela principal

import tkinter as tk
from tkinter import ttk, messagebox

janela = tk.Tk()
janela.title('CALCULADORA')
janela.geometry('350x500+20+20')

valor_display = 0
txt_display = ttk.Entry(font=("Arial", 16, "bold"), justify='right', state='disabled')

txt_display.pack(anchor='n', expand='x')



janela.mainloop()