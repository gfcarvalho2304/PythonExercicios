def titulo(texto): # print com texto em amarelo entre duas cadeias de caracteres na cor verde
    print('\033[34m-=\033[m'*27)
    print(f'\033[33m{texto.center(50).upper()}\033[m')
    print('\033[34m-=\033[m'*27)


def linha(tam=42): # linha com -= com valor padrão de 42 caracteres editavel
    print('\033[34m-=\033[m'*tam)


def erro(texto): # print na cor vermelha
    print(f'\033[31m{texto}\033[m')


def sucesso(texto): # print na cor verde
    print(f'\033[32m{texto}\033[m')


def texto(texto): # print na cor amarela
    print(f'\033[33m{texto}\033[m')

def azul(texto): # print na cor amarela
    print(f'\033[34m{texto}\033[m')


def leia(texto): # input com texto na cor amarela
    t = input(f'\033[33m{texto}\033[m')
    return t


def traco(tam=0): #desenha os traços da palavra
    print('— '*tam)

def enforca(tam=6):
    if tam == 6:
        print()
        azul("|----- ")
        azul("|    | ")
        azul("|      ")
        azul("|      ")
        azul("|      ")
        azul("|      ")
        azul("_      ")
        print()
    elif tam == 5:
        print()
        azul("|----- ")
        azul("|    | ")
        azul("|    O ")
        azul("|      ")
        azul("|      ")
        azul("|      ")
        azul("_      ")
        print()
    elif tam == 4:
        print()
        azul("|----- ")
        azul("|    | ")
        azul("|    O ")
        azul("|    | ")
        azul("|      ")
        azul("|      ")
        azul("_      ")
        print()
    elif tam == 3:
        print()
        azul("|----- ")
        azul("|    | ")
        azul("|    O ")
        azul("|   /| ")
        azul("|      ")
        azul("|      ")
        azul("_      ")
        print()
    elif tam == 2:
        print()
        azul("|----- ")
        azul("|    | ")
        azul("|    O ")
        azul("|   /|\ ")
        azul("|      ")
        azul("|      ")
        azul("_      ")
        print()
    elif tam == 1:
        print()
        azul("|----- ")
        azul("|    | ")
        azul("|    O ")
        azul("|   /|\ ")
        azul("|    | ")
        azul("|   /  ")
        azul("_      ")
        print()
    elif tam ==0:
        print()
        titulo('Que pena...')
        erro("                  |----- ")
        erro("                  |    | ")
        erro("                  |    O ")
        erro("                  |   /|\ ")
        erro("                  |    | ")
        erro("                  |   / \ ")
        erro("                  _       ")
        titulo('Você morreu...')

def vence():
    print()
    titulo('Parabéns!')
    sucesso("                      \O/ ")
    sucesso("                       | ")
    sucesso("                       | ")
    sucesso("                      / \ ")
    titulo('Você venceu!')

