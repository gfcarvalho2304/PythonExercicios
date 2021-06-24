from formata import *                        #importa pacote de formatação
from cadastro import *                       #importa o pacote de cadastro das palavras
from random import randint
#importa função randint para selecionar aleatoriamente palavas da lista ##

    ############################################
            # VARIÁVEIS DO SISTEMA #
    ############################################

menu = ['Cadastrar nova palavra', 'Jogar', 'Sair'] #opções do menu
indice =[]                                         #Índices das opções
palavras = 'palavras.txt'                          #Arquivo das palavras do jogo
palavra =''                                        #incialização da variável palavra
listaPalavras =[]                                  #Inicializa lista que vai receber as palavras cadastradas
dicionario ='dicionario.txt'                       #Arquivo do dicionário de palavras válidas
palavrasValidas = []                               #Lista que vai receber as palavras do arquivo do dicionário
palavraSecreta=[]
palavraSorteada =[]
auxiliar =[]
listaIndice = []
palpitesAnteriores = []


    ############################################
                # MENU INICIAL #
    ############################################

titulo('Bem vindo ao jogo de Forca!')              #mensagem de boas vindas

linha(27)

for o, opcao in enumerate(menu):
    texto(f'{o+1} - {opcao}')
    indice.append(o+1)

linha(27)

    ############################################################
    # ABRE O ARQUIVO TEXTO E CARREGA AS PALAVRAS EM UMA LISTA #
    ############################################################

if not arquivoExiste(palavras): # se o arquivo texto não existir ele é criado
    criarArquivo(palavras)

a = open(palavras, 'rt')
for l in a:
    listaPalavras.append(l.replace('\n', ''))

    ############################################################
        # ABRE O ARQUIVO DO DICIONÁRIO DE PALAVRAS VÁLIDAS  #
    ############################################################

d = open(dicionario, 'rt', encoding="UTF-8") #necessário parâmetro encoding para reconhecer as palavras do arquivo
for x in d:
    palavrasValidas.append(x.replace('\n', '').upper())

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
            # MENU DO CADASTRO DE PALAVRAS #
        ############################################

        elif resp == 1:

            while True:
                palavra = str(leia('Digite a palavra que gostaria de cadastrar:'))
                if palavra.upper() in listaPalavras:           # verifica se a palavra já existe na lista
                    erro('ERRO! A palavra digitada já existe na lista de plavras.')
                elif palavra.upper() not in palavrasValidas:
                    erro('ERRO! Palavra inválida!')

                elif palavra.isalpha() and len(palavra) > 1:   # verifica se a palavra é do tipo alpha
                                                               # (não numerico ou chars especiais)

                    cadastrarPalavra(palavras, palavra)        #armazena palavra no arquivo texto
                    listaPalavras.append(palavra.upper())      #adiciona a palavra na lista gerada no início do programa

                    continuar = str(leia('Deseja continuar cadastrando?')) # verifica se o usuário deseja continuar
                    while continuar not in 'nNsS':                         # certifica que apenas s ou n será digitado
                        erro('ERRO! Digite apenas S ou N')
                        continuar = str(leia('Deseja continuar cadastrando?'))
                    if continuar in 'nN':
                        break
                else:
                    erro('ERRO! Cadastre apenas palavras válidas!')

            ############################################
                        # ENTRA NO JOGO #
            ############################################
        else:
            r = randint(0, len(listaPalavras) -1) #variavel r recebe um valor aleatório referente ao índice da lista
            sorteada = listaPalavras[r]
            chance = 6

            for letra in sorteada:
                palavraSecreta.append('—')      #preenche a lista com traços com o tamanho da palavra
                palavraSorteada.append(letra)   #preenche a lista com as letras da palavra sorteada
                auxiliar.append(letra)          #preenche a lista auxiliar identica a lista da palavra sorteada


            texto('Palavra Secreta:')
            texto(palavraSecreta) #exibe a lista com os traços
            #print(palavraSorteada) #teste
            #print(sorteada) #teste

            while True:
                enforca(chance)
                chute = leia('Digite o seu chute: ').upper()  # captura o palpite do usuário
                while True:
                    if chute not in palpitesAnteriores:       # Verifica se a letra já foi "chutada" anteriormente
                        palpitesAnteriores.append(chute)
                        break
                    else:
                        erro('Você já chutou esta letra, tente outra!')
                        chute = leia('Digite o seu chute: ').upper()

                if chute in palavraSorteada:                #verifica se o palpite está na palavra sorteada

                    while True:
                        ind = (auxiliar.index(chute)) #caso o palpite esteja correto, captura o indice da palavra onde ele existe
                        palavraSecreta[ind] = chute   #substitui o traço da palavra secreta pelo chute
                        auxiliar[ind] = '—'           #substitui a letra da lista auxiliar por um traço
                        if chute not in auxiliar:     #verifica se após a atualização da auxiliar, a letra ainda existe na lista
                            break                     #se não houver mais ocorrências da letra, sai do loop

                    if palavraSecreta == palavraSorteada: #Jogador vence quando a lista palavra secreta for igual a palavra sorteada
                        texto(palavraSecreta)
                        vence()
                        break
                    else:
                        sucesso('Você Acertou!')
                        texto(f'Palpites Anteriores: {palpitesAnteriores}')
                        texto('Palavra Secreta:')
                        texto(palavraSecreta)
                else:                                   #Se o chute não existir na palavra sorteada:
                    erro('Você errou!')                 #Exibe mensagem derro
                    chance-=1                           #Jogador perde uma chance
                    texto(f'Palpites Anteriores: {palpitesAnteriores}')
                    texto('Palavra Secreta:')
                    texto(palavraSecreta)
                    if chance ==0:                      #Quando acabam as achances
                        enforca(chance)                 #Chama função enforca
                        break

        ############################################
            #  VOLTA AO MENU INICIAL #
        ############################################
        palavraSorteada.clear()                        #Limpa as listas para um novo jogo
        palavraSecreta.clear()
        auxiliar.clear()
        palpitesAnteriores.clear()
        linha(27)
        for o, opcao in enumerate(menu):
            texto(f'{o + 1} - {opcao}')
            indice.append(o + 1)
        linha(27)

titulo('Até a próxima')                                #Mensagem de encerramento do programa









