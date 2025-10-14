class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        print(self.a + self.b )

    def subtracao(self):
        print(self.a - self.b )

    def multiplicacao(self):
        print(self.a * self.b )

    def divisao(self):
        if self.b != 0:
            print(self.a / self.b)
        else:
            print('Erro: divisão por zero!')
print('-'*30)
print('CALCULADORA'.center(30))
print('-'*30)
a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
resultado = Calculadora(a, b)
while True:
    print('-'*30)
    print('MENU'.center(30))
    print('-'*30)

    print('[1] somar os números')
    print('[2] subtrair os números')
    print('[3] multiplicar os números')
    print('[4] dividir os números')
    print('[5] sair do programa')
    decisao = int(input('Decisão: '))
    if decisao == 1:
        resultado.soma()
    elif decisao == 2:
        resultado.subtracao()
    elif decisao == 3:
        resultado.multiplicacao()
    elif decisao == 4:
        resultado.divisao()
    elif decisao == 5:
        print('Saindo do programa...')
        break

