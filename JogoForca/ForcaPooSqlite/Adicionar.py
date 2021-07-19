from formata import *                        #importa pacote de formatação
from cadastro import *                       #importa o pacote de cadastro das palavras


            ############################################
                # CLASSE CADASTRO DE PALAVRAS #
            ############################################

class Cadastrar:
    def __init__(self):

        ############################################
                # VARIÁVEIS DAS CLASSE #
        ############################################

        palavras = 'palavras.txt'       #Arquivo das palavras do jogo
        dicionario = 'dicionario.txt'
        palavrasValidas = []
        listaPalavras = []  # Inicializa lista que vai receber as palavras cadastradas

        ############################################################
        # ABRE O ARQUIVO TEXTO E CARREGA AS PALAVRAS EM UMA LISTA #
        ############################################################

        if not arquivoExiste(palavras):  # se o arquivo texto não existir ele é criado
            criarArquivo(palavras)

        # a = open(palavras, 'rt')
        with open(palavras, 'rt') as a:
            for l in a:
                listaPalavras.append(l.replace('\n', ''))

            ############################################################
            # ABRE O ARQUIVO DO DICIONÁRIO DE PALAVRAS VÁLIDAS  #
            ############################################################

        # d = open(dicionario, 'rt', encoding="UTF-8") #necessário parâmetro encoding para reconhecer as palavras do arquivo
        with open(dicionario, 'rt', encoding="UTF-8") as d:
            for x in d:
                palavrasValidas.append(x.replace('\n', '').upper())

        while True:
            palavra = str(leia('Digite a palavra que gostaria de cadastrar:'))
            if palavra.upper() in listaPalavras:  # verifica se a palavra já existe na lista
                erro('ERRO! A palavra digitada já existe na lista de plavras.')
            elif palavra.upper() not in palavrasValidas:
                erro('ERRO! Palavra inválida!')

            elif palavra.isalpha() and len(palavra) > 1:  # verifica se a palavra é do tipo alpha
            # (não numerico ou chars especiais)

                cadastrarPalavra(palavras, palavra.replace)  # armazena palavra no arquivo texto
                listaPalavras.append(palavra.upper())  # adiciona a palavra na lista gerada no início do programa

                continuar = str(leia('Deseja continuar cadastrando?'))  # verifica se o usuário deseja continuar
                while continuar not in 'nNsS':  # certifica que apenas s ou n será digitado
                    erro('ERRO! Digite apenas S ou N')
                    continuar = str(leia('Deseja continuar cadastrando?'))
                if continuar in 'nN':
                    break
            else:
                erro('ERRO! Cadastre apenas palavras válidas!')

        titulo('Bem vindo ao jogo de Forca!')