from forca.cadastro import *
palavras = 'palavras.txt'
teste=[]
palavra='TESTE'
a = open(palavras,'rt')
for linha in a:
    teste.append(linha.replace('\n', ''))

print(teste)