from formata import *                        #importa pacote de formatação
from random import randint                   #importa função randint para selecionar aleatoriamente palavas da lista ##

            ############################################
                    # CLASSE JOGO DE FORCA  #
            ############################################


class Jogar:
    def __init__(self):

        ############################################
                # VARIÁVEIS DAS CLASSE #
        ############################################

        palavras = 'palavras.txt'  # Arquivo das palavras do jogo
        palavra = ''  # incialização da variável palavra
        listaPalavras = []  # Inicializa lista que vai receber as palavras cadastradas
        dicionario = 'dicionario.txt'  # Arquivo do dicionário de palavras válidas
        palavrasValidas = []  # Lista que vai receber as palavras do arquivo do dicionário
        palavraSecreta = []
        palavraSorteada = []
        auxiliar = []
        listaIndice = []
        palpitesAnteriores = []

        ############################################################
        # ABRE O ARQUIVO TEXTO E CARREGA AS PALAVRAS EM UMA LISTA #
        ############################################################

        with open(palavras, 'rt') as a:
            for l in a:
                listaPalavras.append(l.replace('\n', ''))

        ############################################################
                            # INICIA O JOGO #
        ############################################################

        r = randint(0, len(listaPalavras) - 1)  # variavel r recebe um valor aleatório referente ao índice da lista
        sorteada = listaPalavras[r]
        chance = 6

        for letra in sorteada:
            palavraSecreta.append('—')  # preenche a lista com traços com o tamanho da palavra
            palavraSorteada.append(letra)  # preenche a lista com as letras da palavra sorteada
            auxiliar.append(letra)  # preenche a lista auxiliar identica a lista da palavra sorteada

        texto('Palavra Secreta:')
        texto(palavraSecreta)  # exibe a lista com os traços
        # print(palavraSorteada) #teste
        # print(sorteada) #teste

        while True:
            enforca(chance)
            chute = leia('Digite o seu chute: ').upper()  # captura o palpite do usuário
            while True:
                if chute not in palpitesAnteriores:  # Verifica se a letra já foi "chutada" anteriormente
                    palpitesAnteriores.append(chute)
                    break
                else:
                    erro('Você já chutou esta letra, tente outra!')
                    chute = leia('Digite o seu chute: ').upper()

            if chute in palavraSorteada:  # verifica se o palpite está na palavra sorteada

                while True:
                    ind = (auxiliar.index(
                        chute))  # caso o palpite esteja correto, captura o indice da palavra onde ele existe
                    palavraSecreta[ind] = chute  # substitui o traço da palavra secreta pelo chute
                    auxiliar[ind] = '—'  # substitui a letra da lista auxiliar por um traço
                    if chute not in auxiliar:  # verifica se após a atualização da auxiliar, a letra ainda existe na lista
                        break  # se não houver mais ocorrências da letra, sai do loop

                if palavraSecreta == palavraSorteada:  # Jogador vence quando a lista palavra secreta for igual a palavra sorteada
                    texto(palavraSecreta)
                    vence()
                    break
                else:
                    sucesso('Você Acertou!')
                    texto(f'Palpites Anteriores: {palpitesAnteriores}')
                    texto('Palavra Secreta:')
                    texto(palavraSecreta)
            else:  # Se o chute não existir na palavra sorteada:
                erro('Você errou!')  # Exibe mensagem derro
                chance -= 1  # Jogador perde uma chance
                texto(f'Palpites Anteriores: {palpitesAnteriores}')
                texto('Palavra Secreta:')
                texto(palavraSecreta)
                if chance == 0:  # Quando acabam as achances
                    enforca(chance)  # Chama função enforca
                    break

        titulo('Bem vindo ao jogo de Forca!')