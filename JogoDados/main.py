from rolaDados import Dado

menu = ['D-4', 'D-6', 'D-8', 'D-10', 'D-12', 'D-20', 'D-100']

print('Selecione o seu tipo de dado: ')
for i in range(len(menu)):
    print(f'[{menu[i]}]', end=' ')
print()

numFaces = int(input('Número de faces: '))
qtdDados = int(input('Digite a quantidade de dados que gostaria de rolar: '))


jogo = Dado(tipo=numFaces, qtd=qtdDados)

jogo.RolaDados()
