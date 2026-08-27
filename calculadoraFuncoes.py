# CalculadoraFunções

class HistoricoOperacoes:
    def __init__(self, nome='historico.txt'):
        self.historico = []
        self.arq = nome

    def adicionar(self, numero1, numero2, operacao, resultado, raiz=True):
        if not raiz:
            self.historico.append(f'operação: {numero1} {operacao} {numero2} = {resultado}')
        else:
            self.historico.append(f'raiz de índice {numero2} de {numero1} = {resultado}')
        try:
            a = open(self.arq, 'at+')
        except:
            print('Houve um ERRO na abertura do arquivo!')
        else:
            try:
                a.write(f'{self.historico[0]}\n')
            except:
                print('Houve um ERRO na hora de escrever os dados!')
            else:
                a.close()
        self.historico.clear()

    def mostrar(self):
        try:
            a = open(self.arq, 'rt')
        except:
            print('ERRO ao ler o arquivo')
        else:
            for linha in a:
                print(linha)
        finally:
            a.close()

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

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')