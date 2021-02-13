from random import randint

VecRaces = []
VecPilotos = []
VecTempos = []

def menu():
    print("===========")
    print("MENU")
    print("===========")
    print("1.Introdução \n2.Geração de dados\n3.Alterar dados\n4.Eliminar dados")
    print("5.Consultar\n6.Pesquisar\n7.grelha de classificação\n8.Guardar em ficheiro de texto")
    print("9.Carregar dados de ficheiros\n10.Sair")
    print("-----------")


def introducao(Redbull):
    Redbull = {}
    
    for i in range(0, 7):
        print(f"{i + 1}º corrida")
        cidade = str(input('Cidade: '))
        vencedor = str(input('Vencedor: '))
        tempo = float(input('Tempo (minutos. segundos): '))

        VecRaces.append(cidade)
        VecPilotos.append(vencedor)
        VecTempos.append(tempo)
        if i==7:
            return
    Redbull = {'Cidade': VecRaces, 'Vencedor': VecPilotos, 'Tempo': VecTempos}

    return Redbull

def geracao(Redbull):
    VecRaces = []
    VecPilotos = []
    VecTempos = []
    Cities = ["Lisboa", "Berlim", "Paris", "Porto", "Moscovo", "Roma", "Londres", "Manchester", "Liverpool", "Miami", "Los Angeles", "Rio de Janeiro", "Buenos Aires", "Cairo", "New Mexico", "Marselha", "Toronto", "Dublin", "Reykjavik", "New York", "Minas Gerais"]
    Winners = ["Kirby Chambliss", "Pete McLeod", "Matt Hall", "Yoshihide Muroya", "Matthias Dolderer", "Michael Goulian", "Nicolas Ivanoff", "Florian Bergér", "Paul Bonhomme", "Péter Besenyei", "Mélanie Astles", "Nigel Lamb", "Mikaël Brageot", "François Le Vot", "Petr Kopfstein", "Juan Velarde", "Luke Czepiela"]

    for j in range(0, 8):
        cid = Cities[randint(1, len(Cities)-1)]
        win = Winners[randint(1, len(Winners)-1)]
        time = randint(1, 30)
        VecRaces.append(cid)
        VecPilotos.append(win)
        VecTempos.append(time)
        Redbull = {'Cidade': VecRaces, 'Vencedor': VecPilotos, 'Tempo': VecTempos}
    print(f'\n{Redbull}\n')

    
    input("Dados gerados! ")    

def alterar(Redbull, corrida_alterar, posicao_alterar):
    print("\033[35mDADOS ANTIGOS:\033[m")
    print(f'{corrida_alterar}º Corrida')
    for k, v in Redbull.items():
        print(f'{k}:{v[posicao_alterar]}')

    op = str(input("Tem a certeza que quer alterar estes dados? (s/n) "))
    if op == 's':
        ci = str(input('Cidade: '))
        ve = str(input('Vencedor: '))
        t = float(input('Tempo(minutos.segundos): '))
        Redbull['Cidade'][posicao_alterar] = ci
        Redbull['Vencedor'][posicao_alterar] = ve
        Redbull['Tempo'][posicao_alterar] = t
        input("MODIFICADO COM SUCESSO!!!")

def eliminar(Redbull, posicao_eliminar, corrida_eliminar):
    op = str(input("Tem a certeza que quer eliminar estes dados? (s/n) "))
    print(f'{corrida_eliminar}º Corrida')
    for k, v in Redbull.items():
        print(f'{k}:{v[posicao_eliminar]}')
    if op == 's':
        del  Redbull['Cidade'][posicao_eliminar]
        del  Redbull['Vencedor'][posicao_eliminar]
        del  Redbull['Tempo'][posicao_eliminar]

def consultar(vecRaces, vecPilotos, vecTempos):
    print('-' * 100)
    print('               Cidade         Vencedor         Tempo')
    for i in range(0, 8):
        print(f'{i + 1} corrida      {vecRaces[i]}            {vecPilotos[i]}          {vecTempos[i]}')
    print('-' * 100)


def pesquisar(Redbull, corrida_):
    print(f"Dados da {corrida_}º corrida")
    for k, v in Redbull.items():
        print(f'{k}:{v[corrida_]}')
    
def guardar_em_ficheiro_texto(Redbull):
    print("A guardar ficheiro.....")
    ficheiro = open("redbullairrace.txt", "w")

    for i in range(0,2):
        for j in range(0,2):
            ficheiro.write(f'{Redbull[j][i]}; {Redbull[j][i]}; {Redbull[j][i]}')
    
    ficheiro.close()

    
    input("Ficheiro guardado com sucesso! ")

def grelha_de_classificacao(Redbull):
    for i in range(0,7):
        if Redbull['Tempo'][i] > Redbull['Tempo'][i+1]:
            Redbull['Vencedor'][i+1] = a
            a = Redbull['Vencedor'][i]
    #sorted(Redbull['Tempo'])
    #print(f'1ºLugar: {Redbull['Vencedor'][0]} com tempo de {Redbull['Tempo'][0]}')
    #print(f'2ºLugar: {Redbull['Vencedor'][1]} com tempo de {Redbull['Tempo'][1]}')
    #print(f'3ºLugar: {Redbull['Vencedor'][2]} com tempo de {Redbull['Tempo'][2]}')


def carregar_dados_de_ficheiro():
    ficheiro = open("redbullairrace.txt" , "r") # abre o ficheiro

    global contador
    global contador2 
    #global total
    contador = 1

    for linha in ficheiro.readlines(): # corridas
        if (contador > 2): # ignora as duas primeiras linhas
            campos = linha.split(";") 
 
            cidade_ficheiro   = campos[0].rstrip("\n")
            vencedor_ficheiro = campos[1].rstrip("\n")
            tempo_ficheiro    = campos[2].rstrip("\n")

            VecRaces.append(cidade_ficheiro)        # adicionar os dados ao nosso vetor cidades
            VecPilotos.append(vencedor_ficheiro)   # adicionar os dados ao nosso vetor vencedores
            VecTempos.append(tempo_ficheiro)        # adicionar os dados ao nosso vetor tempos

        contador = contador + 1

    if contador == 1:               # acertar o valor do contador de carregar dados para o programa 
        contador2 = contador - 1    # se não carregar dados mete o contador = 0 
    else:
        contador2 = contador -3     # se carregar dados ajeita o contador tirando 3 valores

    ficheiro.close() # fecha o ficheiro
    input("Ficheiro aberto")



Redbull = {}
while True:
    menu()

    opcao = int(input("Escolha a opçao:"))

    if opcao == 1:
        introducao(Redbull)


    elif opcao == 2:
        geracao(Redbull)
    


    elif opcao == 3:
        corrida_alterar = int(input('Qual a corrida que deseja alterar? '))
        posicao_alterar = corrida_alterar - 1
        alterar(Redbull, corrida_alterar, posicao_alterar)


    elif opcao == 4:
        corrida_eliminar = int(input('Qual a corrida que deseja alterar? '))
        posicao_eliminar = corrida_eliminar - 1
        eliminar(Redbull, posicao_eliminar, corrida_eliminar)


    elif opcao == 5:
        consultar(Redbull)
        

    elif opcao == 6:
        opc= int(input("Qual corrida deseja pesquisar (1-8)º ?? "))
        if opc < 1 and opc > 8:
            print("Digite Valores entre 1 e 8. Tente novamente!")
        else:
            pesquisar(Redbull, opc)



    elif opcao == 7:
        grelha_de_classificacao(Redbull)



    elif opcao == 8:
        guardar_em_ficheiro_texto(Redbull)


    elif opcao == 9:
        carregar_dados_de_ficheiro()

    elif opcao == 10:
        break
    
    else:
        print("Opção errada digite números entre 1 e 10")




    




        

   