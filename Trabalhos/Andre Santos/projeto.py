import os, random

def limpa_ecra():
    os.system("cls")


def cabecalho(texto):
    limpa_ecra()
    print("="*25)
    print(texto)
    print("="*25)


def main():
    #definir a lista global
    global chave 
    chave = []
    
    while True:
        cabecalho("Menu")
        print("1. Introdução de dados")
        print("2. Alterar dados")
        print("3. Eliminar dados")
        print("4. Consultar")
        print("5. Verifique a sua chave")
        print("6. Guardar em ficheiro de texto")
        print("7. Carregar dados do ficheiro")
        print("8. Sair")

        opcao = int(input("Opção (1...8):"))

        if opcao == 1:
            introduzir_dados()
        elif opcao == 2:
            alterar_dados()
        elif opcao == 3:
            eliminar_dados()
        elif opcao == 4:
            consulta(0)
        elif opcao == 5:
            verificar_chave()
        elif opcao == 6:
            guardar_ficheiro()
        elif opcao == 7:
            abrir_ficheiro()
        elif opcao == 8:
            break
        else:
            print("opção errada!")
            input()

def introduzir_dados():
    while True:
        cabecalho("INTRODUZIR DADOS")
        print("Como pretende gerar a sua chave:")
        print("1. Gerar chave automáticamente")
        print("2. Criar chave manualmente")
        print("3. Sair")

        opcao = int(input("Opção (1...3):"))

        if opcao == 1:
            gerar_auto() # Cria automáticamente a chave 
        elif opcao == 2:
            manual() # O utilizador introduz a sua chave
        elif opcao == 3:
            break
        else:
            print("Opção errada!")
            input()

def gerar_auto():
    n_vezes = int(input(("Quantas chaves pretende gerar:")))
    limite = 50
    for i in range(n_vezes):
        #Declara a lista e limpa a lista
        registo = []
        for a in range(7):
            while True:
                #gerar as estrelas 
                if a > 4:
                    limite = 12
                #gerar números aleatórios 
                numero_aleatorio = random.randint(1, limite)

                #Verifica se o numero aleatório já existe
                existe = False
                for numero in registo:
                    if numero == numero_aleatorio:
                        existe = True
                        break

                #Caso não exista adiciona adiciona a lista
                if existe == False:
                    registo.append(numero_aleatorio)
                    break
        #Adiciona os registos finais a lista 
        chave.append(registo)

    print("chave criada com sucesso!")
    print("Enter p/terminar...")
    input()
    

def manual():
    n_vezes = int(input(("Quantas chaves pretende inserir:")))
    contador = len(chave) + 1
    for i in range(n_vezes):
        registo = []
        print(str(contador) +"ºRegisto:")
        for a in range(7):    
            while True:
                #Atualiza o valor da condição para as estrelas
                if a > 4:
                    limite = 13
                    mostrar_num_intervalo = 12
                else:
                    limite = 51 #usado na condição
                    mostrar_num_intervalo = 50 #apresenta ao utilizador os números que pode introduzir

                numero = int(input(str(a + 1) + "ºNumero(1.."+ str(mostrar_num_intervalo) +"):"))

                #Verifica se o número está entre 1 e 50 ou 1 e 13
                if numero <= 0 or numero >= limite:
                    continue

                #Verifica se o numero aleatório já existe
                existe = False
                for num in registo:
                    if num == numero:
                        existe = True
                        print("O número já foi introduzido!")
                        break

                #Caso não exista adiciona adiciona a lista
                if existe == False:
                    registo.append(numero)
                    break
        #Adiciona os registos finais a lista 
        chave.append(registo)
        contador = contador + 1
        print("chave criada com sucesso!")
    print("Enter p/terminar...") 
    input()

def consulta(n = 1):

    if n == 0:#Utilizar este procedimento noutras funcoes sem o cabeçalho 
        cabecalho("CONSULTA")

    print("#      Numeros               Estrelas ")
    print("-"*38)
    for i in range(len(chave)):
        numeros = ""
        estrelas =""
        for a in range(len(chave[i])):
            if a <= 4:
                #Concatenação dos numeros
                numeros = numeros + str(chave[i][a]) + " "
            else: 
                #Concatenação das estrelas
                estrelas = estrelas + str(chave[i][a]) + " "
        #Mostra ao utilizador os números e as estrelas
        print((i + 1)," "*(5-len(str(i + 1))),
              numeros, " "*(20-len(numeros)),
              estrelas)

    if n == 0:#Utilizar este procedimento noutras funcoes sem de dar o enter 
        print("Enter p/terminar...")
        input()

def alterar_dados():
    cabecalho("ALTERAR DADOS")
    consulta()
    reg = [] # criação da lista
    p = 51 #usado na condição
    m = 50 #usado pra apresentar ao utilizador os números que pode introduzir
    n = len(chave) + 1

    while True: 
        registo = int(input("Nº do Registo a Alterar(#):"))
        #Verifica se o registo introduzido é valido
        if registo > 0 and registo < n:
            break
        else:
            print("Valor introduzido inválido!")

    registo = registo - 1
    for a in range(len(chave[registo])):
        while True:
            #Atualiza o valor da condição para as estrelas
            if a > 4:
                p = 13
                m = 12

            novo_numero = int(input(str(a + 1) + "ºNumero(1.."+ str(m) +"):"))

            #Verifica se o número está entre 1 e 50 ou 1 e 13
            if novo_numero <= 0 or novo_numero >= p:
                continue

            #Verifica se o numero aleatório já existe
            existe = False
            for num in reg:
                if num == novo_numero:
                    existe = True
                    print("O número já foi introduzido!")
                    break

            #Caso não exista adiciona adiciona a lista
            if existe == False:
                reg.append(novo_numero)
                break

    chave[registo] = reg
    print("Chave alterada com sucesso!")
    print("Enter p/terminar...")
    input()


def eliminar_dados():
    cabecalho("ELIMINAR DADOS")
    consulta()
    numeros =""
    estrelas =""
    n = len(chave) + 1
    while True: 
        registo = int(input("Nº do Registo a Eliminar(#):"))
        #Verifica se o registo introduzido é valido
        if registo > 0 and registo < n:
            break
        else:
            print("Valor introduzido inválido!")

    registo = registo - 1
    for i in range(len(chave[registo])):
        if i <= 4:
            numeros = numeros + str(chave[registo][i]) + " "
        else: 
            estrelas = estrelas + str(chave[registo][i]) + " "

    print("Registo a eliminar:")
    print("Numeros.......:", numeros)
    print("Estrelas.....:", estrelas)

    chave.pop(registo)
    print("Registo eliminado com sucesso!")
    print("Enter p/terminar...") 
    input()

def chave_sorteio():
    limite = 50
    #Declara a lista e limpa a lista
    registo = []
    for a in range(7):
        while True:
            #gerar as estrelas 
            if a > 4:
                limite = 12
            #gerar números aleatórios 
            numero_aleatorio = random.randint(1, limite)

            #Verifica se o numero aleatório já existe
            existe = False
            for numero in registo:
                if numero == numero_aleatorio:
                    existe = True
                    break

            #Caso não exista adiciona adiciona a lista
            if existe == False:
                registo.append(numero_aleatorio)
                break
    #retorna o registo
    return registo

def verificar_chave():
    """Um numero da chave é comparado a cada número do prémio e passa para o seguinte."""
    chave_sort = chave_sorteio()
    print(f"Chave vencedora: {chave_sort}")
    
    for a in range(len(chave)):
        numeros_acertados = ""
        for i in range(len(chave[a])):
            #Restringe a procura, numeros são comparados a numeros e estrelas são comparadas as estrelas
            if i > 4:
                posicao = 5
                n = 7
            else:
                posicao = 0
                n = 5

            while posicao != n:
                if chave[a][i] == chave_sort[posicao]:  
                    numeros_acertados = numeros_acertados + str(chave_sort[posicao]) + " "
                posicao = posicao + 1

        if  numeros_acertados != "":
            print(f"Na chave: {chave[a]} acertou o {numeros_acertados}")

    print("Enter p/terminar...")
    input()

def guardar_ficheiro():
    cabecalho("GUARDAR FICHEIRO")

    ficheiro = open("chaves.txt", "w")

    ficheiro.write("Numeros, Estrelas\n")

    # percorre a lista
    for i in range(len(chave)):
        ficheiro.write(str(chave[i][0]) + ", " + 
        str(chave[i][1]) + ", " + 
        str(chave[i][2]) + ", " +
        str(chave[i][3]) + ", " +
        str(chave[i][4]) + ", " +
        str(chave[i][5]) + ", " +
        str(chave[i][6]) + "\n")

    ficheiro.close()
    # pausa
    print()
    print("Ficheiro guardado!")
    input("ENTER p/ terminar...")


def abrir_ficheiro():
    cabecalho("ABRIR FICHEIRO")
    import pathlib

    fic = pathlib.Path("chaves.txt")

    if fic.is_file():
        ficheiro = open("chaves.txt", "r")

        # percorrer todo o ficheiro de texto
        contador = 1
        for linha in ficheiro.readlines():
            if contador > 1: # ignorar a 1ª linha
                lista_campos = linha.split(",") 
                registo = [int(lista_campos[0]),
                int(lista_campos[1]),
                int(lista_campos[2]),
                int(lista_campos[3]),
                int(lista_campos[4]),
                int(lista_campos[5]),
                int(lista_campos[6])]

                chave.append(registo)

            contador = contador + 1

        print(chave)
        # pausa
        print()
        print("Ficheiro aberto!")
    else:
        print("Ficheiro não existe!")
    input("ENTER p/ terminar...")

#Programa principal 
main()