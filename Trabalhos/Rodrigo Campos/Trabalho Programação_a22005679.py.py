import os

def limpa():
    os.system('cls')

def cabecalho(texto):
    limpa()
    print("="*30)
    print(" " + texto)
    print("="*30)
    print()

def ler_dados():
    cabecalho("Introduçao dados")

    contador = len(lista_dados) + 1

    while True:
        print("Jogo nº" + str(contador))

        grupo = input("Grupo (0 p / terminar).: ")

        if grupo == str(0):
            break

        selecao1 = input("Seleção 1....:")
        selecao2 = input("Seleção 2....:")
        estadio = input("Estádio.....:")
        espectadores = float(input("Espectadores....:"))
        vips = float(input("Vips......:"))

        Jogo = [grupo, selecao1, selecao2, estadio, espectadores, vips]
        lista_dados.append(Jogo)
        
        contador = contador + 1
        print()

def alterar_dados():
    cabecalho("Alterar dados")

    print("#       Grupo        Seleção 1               Seleção 2               Estádio             Espectadores       VIPs")
    print("="*115)

    contador = 1
    for elemento in lista_dados:
        grupo = elemento[0]
        selecao1 = elemento[1]
        selecao2 = elemento[2]
        estadio = elemento[3]
        espectadores = elemento[4]
        vips = elemento[5]

        print(contador, " "*(6-len(str(contador))), grupo, " "*(10-len(str(grupo))), selecao1, " "*(22-len(str(selecao1))), selecao2, " "*(22-len(str(selecao2))), estadio, " "*(18-len(str(estadio))), espectadores, " "*(17-len(str(espectadores))), vips)

        contador = contador + 1

    print()

    Jogo = int(input("Nº Jogo a alterar (#).: "))

    if Jogo > 0 and Jogo < contador :
        Jogo = Jogo - 1
        print()
        print("Grupo........: ", lista_dados[Jogo][0])
        print("Seleção 1....:", lista_dados[Jogo][1])
        print("Seleção 2....:", lista_dados[Jogo][2])
        print("Estádio......:", lista_dados[Jogo][3])
        print("Espectadores.: ", lista_dados[Jogo][4])
        print("VIPs.........: ", lista_dados[Jogo][5])

        print()
        print("Alterar Jogo:")
        novo_grupo = input("Alterar Grupo.....:")
        nova_selecao1 = input("Alterar Seleção 1...:")
        nova_selecao2 = input("Alterar Seleção 2...:")
        novo_estadio = input("Alterar Estádio...:")
        novo_espectadores = float(input("alterar Espectadores...:"))
        novo_vips = float(input("Alterar VIPs...:"))

        lista_dados[Jogo][0] = novo_grupo
        lista_dados[Jogo][1] = nova_selecao1
        lista_dados[Jogo][2] = nova_selecao2
        lista_dados[Jogo][3] = novo_estadio
        lista_dados[Jogo][4] = novo_espectadores
        lista_dados[Jogo][5] = novo_vips

    print()
    print("Jogo alterado!")
    input("ENTER p / continuar....")

def eliminar_dados():
    cabecalho ("Eliminar dados")

    print("#       Grupo        Seleção 1               Seleção 2               Estádio             Espectadores       VIPs")
    print("="*115)

    contador = 1
    for elemento in lista_dados:
        grupo = elemento[0]
        selecao1 = elemento[1]
        selecao2 = elemento[2]
        estadio = elemento[3]
        espectadores = elemento[4]
        vips = elemento[5]

        print(contador, " "*(6-len(str(contador))), grupo, " "*(10-len(str(grupo))), selecao1, " "*(22-len(str(selecao1))), selecao2, " "*(22-len(str(selecao2))), estadio, " "*(18-len(str(estadio))), espectadores, " "*(17-len(str(espectadores))), vips)

        contador = contador + 1

    print() 
    Jogo = int(input("Nº Jogo a eliminar (#).:"))

    if Jogo > 0 and Jogo < contador:
        Jogo = Jogo - 1
        print()
        print("Grupo........: ", lista_dados[Jogo][0])
        print("Seleção 1....:", lista_dados[Jogo][1])
        print("Seleção 2....:", lista_dados[Jogo][2])
        print("Estádio......:", lista_dados[Jogo][3])
        print("Espectadores.: ", lista_dados[Jogo][4])
        print("VIPs.........: ", lista_dados[Jogo][5])
        lista_dados.pop(Jogo)
        
    print()
    print("Jogo eliminado!")
    input("ENTER p / continuar....")

def consultar_dados():
    cabecalho ("Consultar")

    print("#       Grupo        Seleção 1               Seleção 2               Estádio             Espectadores       VIPs")
    print("="*115)

    contador = 1
    for elemento in lista_dados:
        grupo = elemento[0]
        selecao1 = elemento[1]
        selecao2 = elemento[2]
        estadio = elemento[3]
        espectadores = elemento[4]
        vips = elemento[5]

        print(contador, " "*(6-len(str(contador))), grupo, " "*(10-len(str(grupo))), selecao1, " "*(22-len(str(selecao1))), selecao2, " "*(22-len(str(selecao2))), estadio, " "*(18-len(str(estadio))), espectadores, " "*(17-len(str(espectadores))), vips)

        contador = contador + 1

    print()
    input("ENTER p / continuar....")

def pesquisar_dados():
    cabecalho ("Pesquisar")

    print("#       Grupo        Seleção 1               Seleção 2")
    print("="*55)

    contador = 1
    for elemento in lista_dados:
        grupo = elemento[0]
        selecao1 = elemento[1]
        selecao2 = elemento[2]

        print(contador, " "*(6-len(str(contador))), grupo, " "*(10-len(str(grupo))), selecao1, " "*(22-len(str(selecao1))), selecao2)
        contador = contador + 1

    print()

    Jogo = int(input("Nº Jogo a pesquisar (#).: "))
    limpa()

    if Jogo > 0 and Jogo < contador :
        Jogo = Jogo - 1
        Grupo = lista_dados[Jogo][0]
        selecao1 = lista_dados[Jogo][1]
        selecao2 = lista_dados[Jogo][2]
        estadio = lista_dados[Jogo][3]
        espectadores = lista_dados[Jogo][4]
        vips = lista_dados[Jogo][5]

    print("#       Grupo       Seleção 1       Seleção 2       Estádio       Espectadores       VIPs")
    print("="*92)
    print(Jogo, " "*(6-len(str(contador))), grupo, " "*(10-len(str(grupo))), selecao1, " "*(14-len(str(selecao1))), selecao2, " "*(14-len(str(selecao2))), estadio, " "*(12-len(str(estadio))), espectadores, " "*(17-len(str(espectadores))), vips)

    print()
    input("ENTER p / continuar....")

def totais_espectadores():
    cabecalho ("Totais espectadores")

    soma = 0
    contador = 1
    cont_vips = 0
    for elemento in lista_dados:
        espectadores = elemento[4]
        vips = elemento[5]

        soma = soma + espectadores + vips
        cont_vips = cont_vips + vips

        contador = contador + 1

    print("O Torneio tera uma assistencia de: ", soma, " Espectadores")
    print("Dos ", soma, " espectadores ", cont_vips, " são lugares VIPs")
    print()
    input("ENTER p / continuar....")

def guardar_ficheiro():
    cabecalho("Guardar em ficheiro")

    ficheiro = open("lista_de_lista.txt","w",  encoding = 'utf8')
    ficheiro.write("grupo; selecao1; selecao2; estadio; espectadores; vips\n")
    for i in range(len(lista_dados)):
        ficheiro.write(f"{lista_dados[i][0]}; {lista_dados[i][1]}; {lista_dados[i][2]}; {lista_dados[i][3]}; {lista_dados[i][4]}; {lista_dados[i][5]}\n")

    ficheiro.close()

    print()
    print("Ficheiro guardado!")
    input("ENTER p / continuar....")

def carregar_ficheiro():
    cabecalho("Carregar dados do ficheiro")

    ficheiro = open("lista_de_lista.txt", "r", encoding = 'utf8')
    print()
    contador = 1
    for linha in ficheiro.readlines():
        if (contador > 1):
            campos = linha.split(";")
            registo = [campos[0], campos[1], campos[2], campos[3], float(campos[4]), float(campos[5])]
            lista_dados.append(registo)

        contador = contador + 1
    
    print(lista_dados)
    print()
    print("Ficheiro aberto!")
    print()
    input("ENTER p / continuar....")

def main():

    global lista_dados
    lista_dados = []

    while True:
        cabecalho("Menu")
        print(" 1. Introdução dados")
        print(" 2. Alterar dados")
        print(" 3. Eliminar dados")
        print(" 4. Consultar")
        print(" 5. Pesquisar")
        print(" 6. Totais espectadores")
        print(" 7. Guardar em ficheiro")
        print(" 8. Carregar dados do ficheiro")
        print(" 9. Sair")
        print()
        opcao = int(input("Escolha a opção: "))

        if opcao == 1:
            ler_dados()
        elif opcao == 2:
            alterar_dados()
        elif opcao == 3:
            eliminar_dados()
        elif opcao == 4:
            consultar_dados()
        elif opcao == 5:
            pesquisar_dados()
        elif opcao == 6:
            totais_espectadores()
        elif opcao == 7:
            guardar_ficheiro()
        elif opcao == 8:
            carregar_ficheiro()
        elif opcao == 9:
            break
        else:
            print("Opção errada!")


main()