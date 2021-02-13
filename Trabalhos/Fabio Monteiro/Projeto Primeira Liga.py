
vet_clubeA = []         # vetor para guardar o nome 1º Clube
vet_clubeB = []         # vetor para guardar o nome 2º Clube
vet_estadio = []        # vetor para guardar o nome do estadio
vet_espetadores = []    # vetor para guardar o numero de espetadores que atenderam esse jogo
vet_vips = []           # vetor para guardar o numero de espetadores vips que atenderam esse jogo

n_jogos = 0
gerador = 0
contador2 = 0

def limpa_ecra():
    import os                                         
    os.system('cls' if os.name == 'nt' else 'clear')   

def cabecalho():
    print("Jogos        Clube A         Clube B         Estádio                 Espetadores         VIP's")
    print("==============================================================================================")

def int_dados():
    print("Jogos")
    print("="*5)
    limpa_ecra()

    global n_jogos
    global total

    print ("=" * 88)
    print ("                                   INTRODUÇÃO DE DADOS")
    print ("=" * 88)
    print ()

    n_jogos = int(input("Nº de jogos: "))
    total = total + n_jogos     # adicionar o total de dados até ao momento ao total de dados
    
    for i in range(n_jogos):
        print("Jogo " + str(i+1) + ": ")        # Número do jogo
        clubeA = str(input("Clube A: "))        # Introduzir o nome do clube A
        clubeB = str(input("Clube B: "))        # Introduzir o nome do clube B
        estadio = str(input("Estádio: "))       # Introduzir o nome do estádio
        espet = str(input("Espetadores: "))     # Introduzir o número de espetadores
        vips = str(input("VIPs: "))             # Introduzir o número de vips

        vet_clubeA.append(clubeA)       # Adicionar o dado introduzido anteriormente ao vetor clubeA
        vet_clubeB.append(clubeB)       # Adicionar o dado introduzido anteriormente ao vetor clubeB
        vet_estadio.append(estadio)     # Adicionar o dado introduzido anteriormente ao vetor estadio
        vet_espetadores.append(espet)   # Adicionar o dado introduzido anteriormente ao vetor espetadores
        vet_vips.append(vips)           # Adicionar o dado introduzido anteriormente ao vetor vips


def ger_dados():
    import random
    global gerador
    global total
    gerador = 0
    limpa_ecra()
    
    print ("=" * 88)
    print ("                                   GERADOR DE DADOS")
    print ("=" * 88)
    print ()

    clubes = ['Sporting CP', 'FC Porto' , 'SL Benfica', 'SC Braga' , 'Vitória SC' ,'Boavista FC' ,'FC P.Ferreira' ,'Moreirense FC' ,'Santa Clara' ,'SC Farense' ,'CD Tondela' ,'Belenenses SAD' ,'CD Nacional' ,'Gil Vicente FC' ,'Portimonense' ,'FC Famalicão' ,'Marítimo M.' ,'Rio Ave FC']
    estadios = ['José Alvalade','Estádio do Dragão','Estádio da Luz','Municipal de Braga','D. Afonso Henriques','Bessa','Capital do Móvel','Comendador Joaquim','São Miguel','São Luís','João Cardoso','Restelo','Madeira','Cidade de Barçelos','Portimonense SC','Municipal 22 de Junho','Barreiros','Rio Ave Futebol Clube']
    espetador = ['10000','15000','20000','25000','30000','35000','40000','45000','50000']
    vip = ['1000','1500','2000','2500','3000','3500','4000','4500','5000']


    gerador = int(input("Quantos dados vais querer gerar? "))
    total = total + gerador     # adicionar os dados gerados ao numero total de dados
    

    for i in range (gerador):
        cl = random.choice(clubes)      # escolhe um dado gerado da lista de clubes
        cl2 = random.choice(clubes)     # escolhe um dado gerado da lista de clubes
        est = random.choice(estadios)   # escolhe um dado gerado da lista de estadios
        esp = random.choice(espetador)  # escolhe um dado gerado da lista de espetador
        v_ip = random.choice(vip)       # escolhe um dado gerado da lista de vips
        vet_clubeA.append(cl)           # Adicionar o dado gerado anteriormente ao vetor clubeA
        vet_clubeB.append(cl2)          # Adicionar o dado gerado anteriormente ao vetor clubeB
        vet_estadio.append(est)         # Adicionar o dado gerado anteriormente ao vetor estadio
        vet_espetadores.append(esp)     # Adicionar o dado gerado anteriormente ao vetor espetadores
        vet_vips.append(v_ip)           # Adicionar o dado gerado anteriormente ao vetor vips 


    print()
    print("A GERAR DADOS...") 
    import time         
    time.sleep (2)      
        
    print("")
    print("DADOS GERADOS COM  SUCESSO...")
    import time    
    time.sleep (2)

    print()
    input("Pressione Enter para continuar...")

    limpa_ecra()

def alt_dados():
    
    if total == 0:
        limpa_ecra() 

        print ("Introduza primeiro dados...")
        import time
        time.sleep (2)
        limpa_ecra()

    if total != 0:
        limpa_ecra()  
        cabecalho()  

        for i in range (total):     # imprime os dados
            clubeA = vet_clubeA[i]
            clubeB = vet_clubeB[i]
            estadio = vet_estadio[i]
            espet = vet_espetadores[i]
            vips = vet_vips[i]
            print(str(i+1) + " "*(12-len(str(i+1))) , str(vet_clubeA[i]) + " "*(15-len(str(vet_clubeA[i]))) , str(vet_clubeB[i]) + " "*(15-len(str(vet_clubeB[i]))) , str(vet_estadio[i]) + " "*(23-len(str(vet_estadio[i]))) , str(vet_espetadores[i]) + " "*(19-len(str(vet_espetadores[i]))) , str(vet_vips[i]))

        print()
        alterar = input ("Quantos jogos queres alterar? ") 
        
        if alterar == "0": 
            limpa_ecra()

        else:
            for i in range (int(alterar)):
                print()
                n_jogos = input("Que jogo queres alterar? ")
                n_jogos = int(n_jogos) - 1                          # Caso o utilizador queira eliminar jogo 1, temos que subtrair 1 porque esse jogo 1 e o jogo 0 do vetor
                texto_clubeA = vet_clubeA[int(n_jogos)]             # Convertemos para texto para poder alterar o dado 
                texto_clubeB = vet_clubeB[int(n_jogos)]             # Convertemos para texto para poder alterar o dado
                texto_estadio = vet_estadio[int(n_jogos)]           # Convertemos para texto para poder alterar o dado
                texto_espetadores  = vet_espetadores[int(n_jogos)]  # Convertemos para texto para poder alterar o dado      
                texto_vips = vet_vips[int(n_jogos)]                 # Convertemos para texto para poder alterar o dado
                
                print()
                texto_clubeA2 = input("Qual vai ser o clube A novo? ")                          # Introduzimos o nome do clube A novo
                texto_clubeB2 = input("Qual vai ser o clube B novo? ")                          # Introduzimos o nome do clube B novo
                texto_estadio2 = input("Qual vai ser o estádio novo? ")                         # Introduzimos o nome do estadio novo
                texto_espetadores2  = input("Qual vai ser a quantidade nova de espetadores? ")  # Introduzimos o número de espetadores novos
                texto_vips2 = input("Qual vai ser a quantidade nova de VIP's? ")                # Introduzimos o número de vips novos
                
                vet_clubeA.remove(texto_clubeA)             # Removemos os dados antigos do vetor clube A
                vet_clubeB.remove(texto_clubeB)             # Removemos os dados antigos do vetor clube B
                vet_estadio.remove(texto_estadio)           # Removemos os dados antigos do vetor estadio
                vet_espetadores.remove(texto_espetadores)   # Removemos os dados antigos do vetor espetadores    
                vet_vips.remove(texto_vips)                 # Removemos os dados antigos do vetor vips
                vet_clubeA.insert(int(n_jogos), texto_clubeA2)              # Adicionamos os novos dados ao vetor clube A
                vet_clubeB.insert(int(n_jogos), texto_clubeB2)              # Adicionamos os novos dados ao vetor clube B
                vet_estadio.insert(int(n_jogos), texto_estadio2)            # Adicionamos os novos dados ao vetor estadio
                vet_espetadores.insert(int(n_jogos) , texto_espetadores2)   # Adicionamos os novos dados ao vetor espetadores
                vet_vips.insert(int(n_jogos), texto_vips2)                  # Adicionamos os novos dados ao vetor vips
                
    print()
    input("Pressione Enter para continuar...")

    limpa_ecra()  

def eli_dados():
    
    global total

    if  total == 0:
        limpa_ecra() 
        print ("Introduza primeiro dados...")
        import time
        time.sleep(2)
        limpa_ecra()

    if total !=0:
        limpa_ecra() 

        cabecalho()
        for i in range (total): 
            clubeA = vet_clubeA[i]
            clubeB = vet_clubeB[i]
            estadio = vet_estadio[i]
            espet = vet_espetadores[i]
            vips = vet_vips[i]
            print(str(i+1) + " "*(12-len(str(i+1))) , str(vet_clubeA[i]) + " "*(15-len(str(vet_clubeA[i]))) , str(vet_clubeB[i]) + " "*(15-len(str(vet_clubeB[i]))) , str(vet_estadio[i]) + " "*(23-len(str(vet_estadio[i]))) , str(vet_espetadores[i]) + " "*(19-len(str(vet_espetadores[i]))) , str(vet_vips[i]))

        print()
        n_jogos = input("Que jogo queres eliminar? ")

        if n_jogos == "0":
            limpa_ecra()

        else:            
            print()
            n_jogos = int(n_jogos) - 1                 
            texto_clubeA = vet_clubeA[int(n_jogos)]
            texto_clubeB = vet_clubeB[int(n_jogos)]
            texto_estadio = vet_estadio[int(n_jogos)]
            texto_espetadores  = vet_espetadores[int(n_jogos)]         
            texto_vips = vet_vips[int(n_jogos)]                        

            vet_clubeA.remove(texto_clubeA)
            vet_clubeB.remove(texto_clubeB)
            vet_estadio.remove(texto_estadio)
            vet_espetadores.remove(texto_espetadores)         
            vet_vips.remove(texto_vips)                         

            total = total - 1

            op_elim = str(input("Gostaria de eliminar algo mais? "))

            if op_elim == "Sim" or op_elim == "S":
                limpa_ecra()
                eli_dados()   # repete tudo de novo
    
    print()
    input("Pressione Enter para continuar...")

    limpa_ecra()

def consult_dados():
    global total

    if total == 0:
        limpa_ecra() 
        print ("Introduza primeiro dados...")
        print()
        input("Pressione Enter para continuar...")

        limpa_ecra()
        
    if total != 0:
        limpa_ecra()
        cabecalho()
        for i in range(total):  
            print(str(i+1) + " "*(12-len(str(i+1))) , str(vet_clubeA[i]) + " "*(15-len(str(vet_clubeA[i]))) , str(vet_clubeB[i]) + " "*(15-len(str(vet_clubeB[i]))) , str(vet_estadio[i]) + " "*(23-len(str(vet_estadio[i]))) , str(vet_espetadores[i]) + " "*(19-len(str(vet_espetadores[i]))) , str(vet_vips[i]))
        
        print()
        input("Pressione Enter para continuar...")

        limpa_ecra()

def pesq_dados():
    global total 
    global pesquisar

    if total == 0:

        limpa_ecra() 
        print ("Introduza primeiro dados...")
        import time
        time.sleep(2)

    if total != 0:
        while True:
            limpa_ecra()
            print("                       Pesquisar Dados")

            for pesquisar in range (total):
                print(f"{pesquisar + 1} - {pesquisar + 1}º jogo")
                
            print(f"{pesquisar + 2} - Sair") 

            print()  
            op_pesquisa = input("Introduza uma opção: ")

            limpa_ecra()

            if  op_pesquisa <= "0" or op_pesquisa > str(total + 1):       
                continue                                            
            
            if op_pesquisa == str(total + 1):
                break                                               
            
            op = int(op_pesquisa) - 1

            cabecalho()

            clubeA = vet_clubeA[op]
            clubeB = vet_clubeB[op]
            estadio = vet_estadio[op]
            espet = vet_espetadores[op]
            vips = vet_vips[op]
            print(str(op_pesquisa) + " "*(12-len(str(op_pesquisa))) , clubeA + " "*(15-len(str(clubeA))) , clubeB + " "*(15-len(str(clubeB))) , estadio + " "*(23-len(str(estadio))) , espet + " "*(19-len(str(espet))) , vips)
                        
            print()
            input("Pressione Enter para continuar...")

            limpa_ecra()

def totais_espet():

    limpa_ecra()

    soma = 0
    n = len(vet_espetadores)                    # Atribuimos o n neste caso para sabermos o numero de dados do vetor espetadores

    for i in range (n):
        soma = soma + int(vet_espetadores[i])   # Os dados do vetor espetadores vão sendo adicionados à soma, sucessivamente até termos a soma final dos dados todos do vetor de espetadores 
    
    print("O total de espetadores dos "+ str(n) +" jogos são:",soma) 

    print("")
    input("Pressione Enter para continuar...")

    limpa_ecra()

def total_espet_clube():
    
    limpa_ecra()

    max_jogo = max(vet_espetadores)             # Usamos o max para descobrirmos o número maior de espetadores no vetor espetadores

    n = len(vet_espetadores)
    
    print("O máximo de espetadores atinjido nos " + str(n) + " jogos é:", max_jogo)

    print("")
    input("Pressione Enter para continuar...")

    limpa_ecra()

def guar_fich():

    if total == 0:
        print("SEM DADOS PARA GUARDAR \n")

    if total != 0:
        ficheiro = open("primeiraliga.txt","a") 

        for i in range (total): 
            ficheiro.write(f"\n{vet_clubeA[int(i)]};{vet_clubeB[int(i)]};{vet_estadio[int(i)]};{vet_espetadores[int(i)]};{vet_vips[int(i)]}")
        ficheiro.close() 

        print()
        print("A GUARDAR...")
        import time
        time.sleep(2)
        
        print()
        print ("GUARDADO COM SUCCESSO...")
        import time
        time.sleep(2)

    print()
    input("Pressione Enter para continuar...")

    limpa_ecra()  

def carr_fich():
    limpa_ecra()
    ficheiro = open ("primeiraliga.txt" , "r") 

    global contador
    global contador2 
    global total
    contador = 1    

    for linha in ficheiro.readlines(): 
        if (contador > 2):                                  # Ignora as 2 linhas iniciais (cabecalho) que tenho no ficheiro txt
            campos = linha.split(";")                       # Separa os campos por ;
 
            clubeA_ficheiro = campos[0].rstrip("\n")        # No ficheiro o campo na posiçao 0 é o clube A
            clubeB_ficheiro = campos[1].rstrip("\n")        # No ficheiro o campo na posiçao 1 é o clube B
            estadio_ficheiro = campos[2].rstrip("\n")       # No ficheiro o campo na posiçao 2 é o estadio
            espetadores_ficheiro = campos[3].rstrip("\n")   # No ficheiro o campo na posiçao 3 são os espetadores
            vips_ficheiro = campos[4].rstrip("\n")          # No ficheiro o campo na posiçao 4 são os vips


            vet_clubeA.append(clubeA_ficheiro)              # Adicionamos os dados dos clubes A dos ficheiros ao nosso vetor clube A
            vet_clubeB.append(clubeB_ficheiro)              # Adicionamos os dados dos clubes B dos ficheiros ao nosso vetor clube B
            vet_estadio.append(estadio_ficheiro)            # Adicionamos os dados dos estadios dos ficheiros ao nosso vetor estadios
            vet_espetadores.append(espetadores_ficheiro)    # Adicionamos os dados dos espetadored dos ficheiros ao nosso vetor espetadores
            vet_vips.append(vips_ficheiro)                  # Adicionamos os dados dos vips dos ficheiros ao nosso vetor vips


        contador = contador + 1
    
    if contador == 1:                                       # Caso o ficheiro não tenha dados, como nós temos contador = 1  
       contador2 = contador - 1                             # é preciso tiramos esse 1 para o contador voltar para o valor certo sendor contador = 0
    else:
       contador2 = contador - 3                             # Ao carregar os dados do ficheiro, descobri que estavam a ser carregados mais 3 dados sem eles estarem lá
                                                            # então retiramos 3 ao contador para voltar para o número de dados original do ficheiro


    total = total + contador2                               # Adicionamos os dados do ficheiro ao número de dados total

    print()
    
    print("A CARREGAR...") 
    import time
    time.sleep(2)
        
    print()
    print ("CARREGADO COM SUCCESSO...")
    import time
    time.sleep(2)

    print()
    input("Pressione Enter para continuar...")

    limpa_ecra()

def main():
    global total
    total = n_jogos + gerador + contador2

    while True:
        print("="*88)
        print("                                       MENU")
        print("="*88)
        print("1. Introdução de dados")
        print("2. Geração dados (preenchimento dos vetores (lista) ou das matrizes de forma automática)")
        print("3. Alterar dados")
        print("4. Eliminar dados")
        print("5. Consultar")
        print("6. Pesquisa (ver dados de um jogo)")
        print("7. Totais espetadores")
        print("8. Total de espetadores (máximo espetadores)")
        print("9. Guardar em ficheiro")
        print("10. Carregar dados do ficheiro")
        print("11. Sair")

        opcao = int(input("Escolha opção: "))
        limpa_ecra()

        if opcao == 1:
            int_dados()
        elif opcao == 2:
            ger_dados()
        elif opcao == 3:
            alt_dados()
        elif opcao == 4:
            eli_dados()
        elif opcao == 5:
            consult_dados()
        elif opcao == 6:
            pesq_dados()
        elif opcao == 7:
            totais_espet()
        elif opcao == 8:
            total_espet_clube()
        elif opcao == 9:
            guar_fich()
        elif opcao == 10:
            carr_fich()
        elif opcao == 11:
            break
        else:
            print("Opção errada")

main()