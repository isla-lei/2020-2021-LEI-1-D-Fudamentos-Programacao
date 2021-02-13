def cabecalho(texto):
    print("=" * 30)
    print(" " + texto)
    print("=" * 30)


def introduzir_dados():
    cabecalho("Introduzir")
    for i in range (8):
        cidade = str(input("Introduza a cidade da corrida: "))
        nome = str(input("Introduza o nome do piloto que venceu a corrida: "))
        tempo = float(input("Introduza o tempo de corrida do piloto que venceu em segundos: "))
        registo = [cidade, nome, tempo]
        lista_dados.append(registo)
    


def alterar_dados():
    cabecalho("Alterar dados")
    print()
    print("#   Cidade     Nome                      Tempo")
    print("=" * 50)

    contador = 1
    for elemento in lista_dados:
        cidade = elemento[0]
        nome = elemento[1]
        tempo = elemento[2]

        print(contador, " " * (3 - len(str(contador))), cidade, " " * (8 - len(str(cidade))), nome,
              " " * (30 - len(str(nome))), tempo)

        contador = contador + 1
    print()
    registo = int(input("Nº Registo a alterar (#).: "))
    if registo > 0 and registo < contador:
        registo = registo -1
        print()
        print(f"Cidade.....: {lista_dados[registo][0]}")
        print(f"Nome.......: {lista_dados[registo][1]}")
        print(f"Tempo.......: {lista_dados[registo][2]}")

        print()
        print("Alerar registo:")
        nova_cidade = input(" Alterar cidade...........:")
        novo_nome = input(" Alterar nome...............: ")
        novo_tempo = float(input(" Alterar tempo...............: "))

        lista_dados[registo][0] = nova_cidade
        lista_dados[registo][1] = novo_nome
        lista_dados[registo][2] = novo_tempo
        print()
        print("Registo alterado!")
        input("ENTER p/ continuar....")


def eliminar_dados():
    cabecalho("Eliminar dados")
    print()
    print("#   Cidade     Nome                      Tempo")
    print("=" * 50)

    contador = 1
    for elemento in lista_dados:
        cidade = elemento[0]
        nome = elemento[1]
        tempo = elemento[2]

        print(contador, " " * (3 - len(str(contador))), cidade, " " * (8 - len(str(cidade))), nome,
              " " * (30 - len(str(nome))), tempo)

        contador = contador + 1
    print()
    registo = int(input("Nº Registo a eliminar (#).: "))
    if registo > 0 and registo < contador:
        # mostra registo
        registo = registo -1
        print()
        print(f"Cidade.....: {lista_dados[registo][0]}")
        print(f"Nome.......: {lista_dados[registo][1]}")
        print(f"Tempo.......: {lista_dados[registo][2]}")
        lista_dados.pop(registo)
        print()
        print("Registo eiminado!")
        input("ENTER p/ continuar....")


def consulta():
    cabecalho("Consultar")
    print()
    print("#   Cidade     Nome                      Tempo")
    print("=" * 50)

    contador = 1
    for elemento in lista_dados:
        cidade = elemento[0]
        nome = elemento[1]
        tempo = elemento[2]

        print(contador, " " * (3 - len(str(contador))), cidade, " " * (8 - len(str(cidade))), nome,
              " " * (30 - len(str(nome))), tempo)

        contador = contador + 1

    print()
    input("ENTER p / continuar....")


def guardar():
    cabecalho("Guardar em ficheiro de texto")
    ficheiro = open("dados_corrida.txt","w")
    ficheiro.write("cidade; nome; tempo\n")
    for i in range(len(lista_dados)):
        ficheiro.write(f"{lista_dados[i][0]}; {lista_dados[i][1]}; {lista_dados[i][2]}\n")
    ficheiro.close()
    print()
    print("Ficheiro guardado!")
    input("ENTER p/ continuar....")

def carregar():
    cabecalho("Carregar dados do ficheiro")
    ficheiro = open("dados_corrida.txt","r") 
    print()
    contador = 1
    for linha in ficheiro.readlines(): 
        if (contador > 1):
            campos = linha.split(";")
            registo = [str(campos[0]), campos[1].lstrip(), float(campos[2].rstrip("\n"))]
            lista_dados.append(registo)
        contador = contador + 1

    print(lista_dados)
    print()
    print("Ficheiro aberto!")
    print()
    input("ENTER p/ continuar....")
        

def main():
    global lista_dados
    lista_dados = []

    while True:
        cabecalho("MENU")
        print("1.Introduzir dados")
        print("2.Alterar Dados")
        print("3.Eliminar Dados")
        print("4.Consultar")
        print("5.Guardar em ficheiro de texto")
        print("6.Carregar dados do ficheiro")
        print("7.Sair")
        opcao = int(input("Escolha a opção que deseja: "))

        if opcao == 1:
            introduzir_dados()
        elif opcao == 2:
            alterar_dados()
        elif opcao == 3:
            eliminar_dados()
        elif opcao == 4:
            consulta()
        elif opcao == 5:
            guardar()
        elif opcao == 6:
            carregar()
        elif opcao == 7:
            break
        else:
            print("Opção errada")
main()
