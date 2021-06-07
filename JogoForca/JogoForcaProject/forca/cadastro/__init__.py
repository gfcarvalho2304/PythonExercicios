from forca.formata import * # importa biblicate de formatação


def arquivoExiste(nome): # função para verificar se um arquivo existe
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome): # função para criar um arquivo texto
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        erro('Houve um erro na criação do arquivo!')
    else:
        sucesso(f'Arquivo {nome} criado com sucesso!')


def cadastrarPalavra(arq,palavra): # função para escrever palavras em um arquivo texto
    try:
        a = open(arq,'at')
    except:
        erro('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{palavra.upper()}\n')
        except:
            erro('Houve um erro ao cadastrar a palavra!')
        else:
            sucesso(f'Nova palavra {palavra.upper()} adicionada com sucesso!')
            a.close()

