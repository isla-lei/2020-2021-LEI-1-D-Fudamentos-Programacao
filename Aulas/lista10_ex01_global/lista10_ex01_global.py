import os


def limpa_ecra():
    os.system("cls")


def cabecalho(texto):
    limpa_ecra()
    print("="*25)
    print(texto)
    print("="*25)


def ler_dados():
    cabecalho("LER DADOS")

    contador = len(lista_dados) + 1  # quantidade elementos da lista_dados

    while True:
        print("Registo nº ", contador)
        # ou..
        # print(f"Registo nº {contador}")

        numero = int(input(" Numero (0 p/terminar): "))
        if numero == 0:
            break

        nome = input(" Nome.................: ")
        nota = float(input(" Nota.................: "))

        # criar a lista com os dados de um registo (numero, nome, nota)
        registo = [numero, nome, nota]  # ex: [100, "Estudante 1", 15.5]
        # print(registo)

        # adicionar o registo à lista_dados definida no main() como global
        lista_dados.append(registo)
        # print(lista_dados)

        contador = contador + 1


def ver_dados():
    cabecalho("CONSULTA DADOS")

    print("#     Numero      Nome                            Nota")
    print("------------------------------------------------------")

    # percorrer toda a lista
    n = len(lista_dados)  # quantidade elementos da lista_dados
    for i in range(n):  # ciclo de i = 0 até n-1
        numero = lista_dados[i][0]  # numero
        nome = lista_dados[i][1]  # nome
        nota = lista_dados[i][2]  # nota
        print((i+1), " "*(4-len(str(i))),
              numero, " "*(10-len(str(numero))),
              nome, " "*(30-len(nome)),
              nota)

    # pausa
    print()
    input("ENTER p/ terminar...")


def mostra_media():
    cabecalho("MEDIA NOTAS")

    # percorrer toda a lista
    n = len(lista_dados)  # quantidade elementos da lista_dados
    soma = 0
    for i in range(n):  # ciclo de i = 0 até n-1
        soma = soma + lista_dados[i][2] # exemplo:  [100, "Estudante 1", 15.5] -> nota [0][2] -> 15.5
    
    if n > 0:
        media = soma / n
        print(F"Média das notas: {media}")
        # ou..
        # print("Média das notas:", media)
    else:
        print("Sem dados....")

    # pausa
    print()
    input("ENTER p/ terminar...")



def mostra_maximo():
    cabecalho("NOTA MAIOR")


    # percorrer toda a lista
    n = len(lista_dados)  # quantidade elementos da lista_dados

    # assumir que a 1ª nota da lista é o max
    if n > 0:
        max = lista_dados[0][2]
        posicao = 0
    else:
        print("Sem dados....")

    for i in range(n):  # ciclo de i = 0 até n-1
        if lista_dados[i][2] > max:
            max = lista_dados[i][2]
            posicao = i


    print()
    if n >0:
        print(f"Nota maior...: {max}")
        print(f"Numero......: {lista_dados[posicao][0]}")
        print(f"Nome........: {lista_dados[posicao][1]}")
        print(f"Nota........: {lista_dados[posicao][2]}")
    
    # pausa
    print()
    input("ENTER p/ terminar...")

def guardar_ficheiro():
    cabecalho("GUARDAR FICHEIRO")

    ficheiro = open("dados_notas.txt", "w", encoding = 'utf8')

    ficheiro.write("Numero, Nome, Nota\n")

    # percorrer toda a lista atraves da interação dos elementos
    for item in lista_dados:
        ficheiro.write(str(item[0]) + ", " + item[1] + ", " + str(item[2]) + "\n")

    # ou..
    # n = len(lista_dados)
    # for i in range(n):  # ciclo de i = 0 até n-1
    #     ficheiro.write(str(lista_dados[i][0]) + ", " + 
    #     lista_dados[i][1] + ", " + 
    #     str(lista_dados[i][2]) + "\n")

    ficheiro.close()

    # pausa
    print()
    print("Ficheiro guardado!")
    input("ENTER p/ terminar...")

def abrir_ficheiro():
    cabecalho("ABRIR FICHEIRO")

    ficheiro = open("dados_notas.txt", "r", encoding = 'utf8')
    # ficheiro = open("dados_notas.txt", "r")

    # percorrer todo o ficheiro de texto
    contador = 1
    for linha in ficheiro.readlines():
        if contador > 1: # ignorar a 1ª linha
            # print(linha)
            lista_campos = linha.split(",") # separa a linha pelo separador "," e coloca na lista_campos
            # print(lista_campos) 
            # print(lista_campos[1])
            # strip() -> retira espaços brancos
            registo = [int(lista_campos[0]), lista_campos[1].strip(), float(lista_campos[2])]
            # print(registo)
            lista_dados.append(registo)

        contador = contador + 1

    print(lista_dados)
    # pausa
    print()
    print("Ficheiro aberto!")
    input("ENTER p/ terminar...")

def alterar_dados():
    cabecalho("ALTERAR DADOS")


def eliminar_dados():
    cabecalho("ELIMINAR DADOS")


def main():

    # definir a lista global
    global lista_dados
    lista_dados = []

    while True:
        cabecalho("MENU")

        print(" 1. Introduzir dados")
        print(" 2. Ver notas")
        print(" 3. Media notas")
        print(" 4. Nota maxima")
        print(" 5. Guardar em ficheiro")
        print(" 6. Abrir ficheiro")
        print(" 7. Alterar dados")
        print(" 8. Eliminar dados")
        print(" 9. Sair")
        print()

        opcao = int(input(" Escolha opcao: "))

        if opcao == 1:
            ler_dados()
        elif opcao == 2:
            ver_dados()
        elif opcao == 3:
            mostra_media()
        elif opcao == 4:
            mostra_maximo()
        elif opcao == 5:
            guardar_ficheiro()
        elif opcao == 6:
            abrir_ficheiro()
        elif opcao == 7:
            alterar_dados()
        elif opcao == 8:
            eliminar_dados()
        elif opcao == 9:
            break
        else:
            print("opção errada!")


if __name__ == "__main__":
    main()
# ou...
# main()
