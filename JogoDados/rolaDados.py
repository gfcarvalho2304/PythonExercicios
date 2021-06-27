from random import randint
from time import sleep

class Dado:
    def __init__(self, tipo=1, qtd=1):
        self.tipo = tipo
        self.qtd = qtd
        self.dados = [4, 6, 8, 10, 12, 20, 100]
        self.total = 0


    def RolaDados(self):
        if self.tipo in self.dados:
            print(f'Você selecionou {self.qtd} D-{self.tipo}...')
            print()
            sleep(1)
            print('Rolando...')
            print()
            for i in range(0, self.qtd):
                valor = randint(1, self.tipo)
                print(f'[{valor}]', end=' ')
                sleep(1)
                #self.dados.append(valor)
                self.total = self.total + valor
            print()
            print()
            print(f'Total: {self.total}')

        else:
            print('Digite um tipo de dado válido...')

