def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n

def linha(tam=30):
    return'__' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[32m{c} - \033[32m{item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção:')
    return opc








