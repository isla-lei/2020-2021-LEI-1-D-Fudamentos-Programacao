import trab
def arquivoexiste(nome):
    try:
        a = open(nome ,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:

        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo{nome} criado com sucesso!')

def lerarquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        trab.cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())

def cadastrar(arq, nome='desconhecido, idade=0'):
    try:
        a = open(arq,'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};.{trab.idade}\n')
        except:
            print('Houve um ERRO na hora de escrever dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()


