import Adicionar
import Jogo
from formata import *                        #importa pacote de formatação
from cadastro import *                       #importa o pacote de cadastro das palavras
from random import randint                   #importa função randint para selecionar aleatoriamente palavas da lista ##
#from Adicionar import Cadastro

    ############################################
            # VARIÁVEIS DO SISTEMA #
    ############################################

menu = ['Cadastrar nova palavra', 'Jogar', 'Sair'] #opções do menu
indice =[]                                         #Índices das opções



    ############################################
                # MENU INICIAL #
    ############################################

titulo('Bem vindo ao jogo de Forca!')              #mensagem de boas vindas

linha(27)

for o, opcao in enumerate(menu):
    texto(f'{o+1} - {opcao}')
    indice.append(o+1)

linha(27)


    ############################################
    # TRATAMENTO DE ERROS NA SELEÇÃO DE OPÇÕES #
    ############################################

while True:

    try:
        resp =int(leia('Escolha uma opção: '))
    except (ValueError, KeyboardInterrupt):
        erro('ERRO! Opção inválida!')
    else:
        if resp not in indice:
            erro('ERRO! Opção inválida!')

        ############################################
                    # SAI DO PROGRAMA #
        ############################################

        elif resp ==3:
            break

        ############################################
            # CHAMA CLASSE ADICIONAR #
        ############################################

        elif resp == 1:
            Adicionar.Cadastrar()


        ############################################
                    # CHAMA CLASSE JOGO #
        ############################################
        else:
            Jogo.Jogar()

        ############################################
            #  VOLTA AO MENU INICIAL #
        ############################################

        for o, opcao in enumerate(menu):
            texto(f'{o + 1} - {opcao}')
            indice.append(o + 1)
        linha(27)

titulo('Até a próxima')                                #Mensagem de encerramento do programa









