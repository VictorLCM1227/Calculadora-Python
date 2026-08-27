# CalculadoraFunções

class HistoricoOperacoes:
    def __init__(self):
        self.historico = []

    def adicionar(self, numero1, numero2, operacao, resultado, raiz=True):
        if not raiz:
            self.historico.append(f'operação: {numero1} {operacao} {numero2} = {resultado}')
        else:
            self.historico.append(f'raiz de índice {numero2} de {numero1} = {resultado}')

    def mostrar(self):
        for item in self.historico:
            print(item)

    def limpar(self):
        self.historico.clear()

sistema = HistoricoOperacoes()
        
def somar(numero1, numero2):
    soma = numero1 + numero2
    sistema.adicionar(numero1, numero2, operacao='+', resultado=soma)
    return soma

def subtrair(numero1, numero2):
    subtracao = numero1 - numero2
    sistema.adicionar(numero1, numero2, operacao='-', resultado=subtracao)
    return subtracao

def multiplicar(numero1, numero2):
    produto = numero1 * numero2
    sistema.adicionar(numero1, numero2, operacao='*', resultado=produto)
    return produto

def dividir(numero1, numero2):
    resultado = numero1 / numero2
    sistema.adicionar(numero1, numero2, operacao='/', resultado=resultado)
    return resultado

def dividirInteiro(numero1, numero2):
    resultado = numero1 % numero2
    sistema.adicionar(numero1, numero2, operacao='//', resultado=resultado)
    return resultado

def potenciar(numero1, numero2):
    resultado = numero1 ** numero2
    sistema.adicionar(numero1, numero2, operacao='**', resultado=resultado)
    return resultado

def radiciar(numero1, numero2):
    resultado = numero1 ** (1 / numero2)
    sistema.adicionar(numero1, numero2, operacao='√', resultado=resultado)
    return resultado

def porcentagem(numero1, numero2):
    resultado = numero1 * (numero2 / 100)
    sistema.adicionar(numero1, numero2, operacao='%', resultado=resultado)
    return resultado