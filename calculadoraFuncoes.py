# CalculadoraFunções

class HistoricoOperacoes:
    def __init__(self):
        self.historico = []

    def adicionar(self, operacao, valor):
        self.historico.append({"operacao": operacao, "valor": valor})

    def mostrar(self):
        for item in self.historico:
            print(f"Operação: {item['operacao']} | Valor: {item['valor']}")

    def limpar(self):
        








def somar(numero1, numero2):
    soma = numero1 + numero2
    return soma

def subtrair(numero1, numero2):
    subtracao = numero1 - numero2
    return subtracao

def multiplicar(numero1, numero2):
    produto = numero1 * numero2
    return produto

def dividir(numero1, numero2):
    resultado = numero1 / numero2
    return resultado

def dividirInteiro(numero1, numero2):
    resultado = numero1 % numero2
    return resultado

def potenciar(numero1, numero2):
    resultado = numero1 ** numero2
    return resultado

def radiciar(numero1, numero2):
    resultado = numero1 ** (1 / numero2)
    return resultado

def porcentagem(numero1, numero2):
    resultado = numero1 * (numero2 / 100)
    return resultado