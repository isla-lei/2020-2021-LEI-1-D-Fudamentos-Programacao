#def ler_dados(lista_dados): # senão definir lista_dados como global
def ler_dados(): # se definir lista_dados como global
    
    # repetir até que o utilizador introduza o zero para o campo numero
    while True:  # ciclo infinito 

        tam = len(lista_dados)
        print("Registo nº", tam + 1)

        numero = int(input("Numero: "))
        if numero == 0:
            break # para o ciclo while

        nome = input("Nome: ")
        salario = float(input("Salario: "))
        irs = salario * 20 / 100
        print("IRS: ", irs)
        ss = salario * 11 / 100
        print("SS: ", ss)

        registo = [numero, nome, salario, irs, ss]

        lista_dados.append(registo)
        print(lista_dados)
    
def ver_dados():

    # percorrer toda a lista
    print("Numero   Nome                            Salario     IRS         Seg Social")
    print("="*80)

    for item in lista_dados:
        print(item[0], " "*(7-len(str(item[0]))), 
                item[1], " "*(30-len(item[1])), 
                item[2], " "*(10-len(str(item[2]))),
                item[3], " "*(10-len(str(item[3]))),
                item[4])

    # outra forma
    #for i in range(len(lista_dados)):
    #    print(lista_dados[i][0],lista_dados[i][1], lista_dados[i][2],lista_dados[i][3], lista_dados[i][4])


    #pausa
    input("ENTER p/ continuar")

def salario_maximo(lista):

    max = 0
    # para todos os casos, podemos pressopor que o max é o 1º, para depois
    # percorrer toda a restante lista e comparar

    tam = len(lista)
    if tam > 0:
        max = lista[0][2] #-> salario o 1º funcionario

    # percorrer a lista e comparar os salarios com o max
    for i in range(len(lista)):
        if lista[i][2] > max:
            max = lista[i][2]
    
    # como é uma função tem que ter return
    return max


def main():

    global lista_dados # definir como global
    lista_dados = []

    while True:
        print("1. Introduzir dados")
        print("2. Ver dados")
        print("3. Salário Maior")
        print("4. Guardar dados em ficheiro")
        print("5. Recuperar dados do ficheiro")
        print("6. Sair")

        opcao = int(input("Escolha opção: "))
        if opcao == 1:
            #ler_dados(lista_dados) # senão definir lista_dados como global
            ler_dados() # se definir lista_dados como global
        elif opcao == 2:
            ver_dados()      
        elif opcao == 3:
            max_sal = salario_maximo(lista_dados)  
            print("Salario maximo: ", max_sal)    
            input("ENTER p/ continuar")
        else:
            break # termina o while


if __name__ == "__main__":
    main()
# ou...
# main()

