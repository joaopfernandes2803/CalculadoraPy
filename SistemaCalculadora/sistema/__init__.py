from SistemaCalculadora.arquivo import salvar_historico, ler_historico, limpar_tudo
from time import sleep

class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return'\033[31mErro: divisão por zero!\033[m'

def sistema():
    print('\033[34m-\033[m'*30)
    print('\033[33mCALCULADORA\033[m'.center(40))
    print('\033[33m-\033[m' * 30)
    sleep(0.8)
    while True:
        try:
            a = float(input("Digite um numero: "))
            b = float(input("Digite outro numero: "))
            break
        except ValueError:
            print('\033[31mErro: Digite um numero inteiro.\033[m')

    sleep(1)
    resultado = Calculadora(a, b)
    lista=[]

    while True:
        print('\033[34m-\033[m' * 30)
        print('\033[33mMENU\033[m'.center(30))
        print('\033[33m-\033[m' * 30)

        sleep(0.6)

        print('[1] Somar os números')
        print('[2] Subtrair os números')
        print('[3] Multiplicar os números')
        print('[4] Dividir os números')
        print('[5] Mostrar histórico')
        print('[6] Salvar histórico em arquivo')
        print('[7] Ler histórico do arquivo')
        print('[8] Limpar historico')
        print('[9] Sair do programa')
        try:
            decisao = int(input('Decisão: '))
        except ValueError:
            print('\033[31mErro: Digite um numero inteiro de 1 a 9\033[m')
            continue

        if decisao == 1:
            res = resultado.soma()
            print(f'Resultado: {res}')
            lista.append(f'Soma: {res}')
        elif decisao == 2:
            res = resultado.subtracao()
            print(f'Resultado: {res}')
            lista.append(f"Subtração: {res}")
        elif decisao == 3:
            res = resultado.multiplicacao()
            print(f'Resultado: {res}')
            lista.append(f"Multiplicação: {res}")
        elif decisao == 4:
            res = resultado.divisao()
            print(f'Resultado: {res:.2f}')
            lista.append(f"Divisão: {res:.2f}")
        elif decisao == 5:
            print('Histórico: \n')
            for item in lista:
                print('-', item)
        elif decisao == 6:
            salvar_historico(lista)
        elif decisao == 7:
            ler_historico()
        elif decisao == 8:
            limpar_tudo(lista)
        elif decisao == 9:
            print('Saindo do programa...')
            sleep(1.5)
            print('FIM')
            break


