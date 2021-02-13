lista_dados = [[0, 0, 0]]
contador = 0
def main():
    while True:
        print("1. Adicionar dados")
        print("2. Alterar dados")
        print("3. Eliminar dados")
        print("4. Consultar dados")
        print("5. Sair")
        opcao = int(input("Escolha opção: "))
        if opcao == 1:
            adicionar_dados()
        elif opcao == 2:
            alterar_dados()
        elif opcao == 3:
            eliminar_dados()
        elif opcao == 4:
            consultar_dados()
        elif opcao == 5:
            break
        else:
            print("Opção errada!")  

def adicionar_dados():

    while True:

        print("Registo nº " + str(len(lista_dados)))
        print("Introduza -1 para terminar:")
        nome = input("Nome..............:")
        inicio_do_mandato = int(input("Ano do inicio do mandato...:"))
        fim_do_mandato = int(input("Ano do fim do mandato......:"))
        registo = [nome, inicio_do_mandato, fim_do_mandato]
        lista_dados.append(registo)

        if nome == -1 or inicio_do_mandato ==-1 or fim_do_mandato ==-1:
            break

        print()
        input("ENTER p / continuar....")

def alterar_dados():
    

    print("#       Nome                   Inicio do Mandato              Fim do Mandato")
    print("="*76)

    contador = 1
    for elemento in lista_dados:
        nome = elemento[0]
        inicio_do_mandato = elemento[1]
        fim_do_mandato = elemento[2]
        

        print(contador, " "*(6-len(str(contador))), nome, " "*(21-len(str(nome))), inicio_do_mandato, " "*(29-len(str(inicio_do_mandato))), fim_do_mandato)

        contador = contador + 1

    print()


    presidente = int(input("Nº presidente a alterar (#).: "))

    if presidente > 0 and presidente < contador :
        presidente = presidente - 1
        print()
        print("Nome................:", lista_dados[presidente][0])
        print("Inicio do mandato...:", lista_dados[presidente][1])
        print("Fim do mandato......:", lista_dados[presidente][2])
        

        print()
        print("Alterar presidente:")
        nome1 = input("Alterar nome.............................:")
        inicio_do_mandato1 = input("Alterar inicio do mandato...:")
        fim_do_mandato1 = input("Alterar fim do mandato.........:")
        

      
        lista_dados[presidente][0] = nome1
        lista_dados[presidente][1] = inicio_do_mandato1
        lista_dados[presidente][2] = fim_do_mandato1
        

    print()
    print("Presidente alterado!")
    input("ENTER p / continuar....")

def eliminar_dados():
    

    print("#       Nome                   Inicio do Mandato              Fim do Mandato")
    print("="*76)
    contador = 1
    for elemento in lista_dados:
        nome = elemento[0]
        inicio_do_mandato = elemento[1]
        fim_do_mandato = elemento[2]
        

        print(contador, " "*(6-len(str(contador))), nome, " "*(21-len(str(nome))), inicio_do_mandato, " "*(29-len(str(inicio_do_mandato))), fim_do_mandato)


        contador = contador + 1

    print()
    
    presidente = int(input("Nº presidente a alterar (#).: "))

    if presidente > 0 and presidente < contador :
        presidente = presidente - 1
        print()
        print("Nome................:", lista_dados[presidente][0])
        print("Inicio do mandato...:", lista_dados[presidente][1])
        print("Fim do mandato......:", lista_dados[presidente][2])
        lista_dados.pop(presidente)
        
    print()
    print("Presidente eliminado!")
    input("ENTER p / continuar....")

def consultar_dados():
    
    print("#       Nome                   Inicio do Mandato              Fim do Mandato")
    print("="*76)
    n = len(lista_dados)
    
    contador = 0

    for i in range(n):

        contador = contador + 1

        print(contador, " "*(6-len(str(contador))),lista_dados[i][0], " "*(21 - len(str(lista_dados[i][0]))),
            lista_dados[i][1], " "*(29 - len(str(lista_dados[i][1]))),
            lista_dados[i][2])
    input("ENTER p/ terminar...")


main()