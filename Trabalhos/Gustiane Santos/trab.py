from trab01 import *
from Cadastrador import *
from time import sleep

arq = 'Gustiane.santos'
if not arquivoexiste(arq):
    criararquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoa nova','Sair do sistema'])
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo!
        lerarquivo(arq)

    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome)


    elif resposta == 3:
        cabeçalho('Saída do sistema... Até logo')
        break
    else:
        print('Erro! Digite uma opção válida!')
    sleep(4)







