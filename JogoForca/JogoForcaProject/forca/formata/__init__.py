def titulo(texto): # print com texto em amarelo entre duas cadeias de caracteres na cor verde
    print('\033[32m-=\033[m'*27)
    print(f'\033[33m{texto.center(50).upper()}\033[m')
    print('\033[32m-=\033[m'*27)


def linha(tam=42): # linha com -= com valor padrão de 42 caracteres editavel
    print('\033[32m-=\033[m'*tam)


def erro(texto): # print na cor vermelha
    print(f'\033[31m{texto}\033[m')


def sucesso(texto): # print na cor verde
    print(f'\033[32m{texto}\033[m')


def texto(texto): # print na cor amarela
    print(f'\033[33m{texto}\033[m')


def leia(texto): # input com texto na cor amarela
    t = input(f'\033[33m{texto}\033[m')
    return t

def traco(tam=0): #desenha os traços da palavra
    print('— '*tam)


