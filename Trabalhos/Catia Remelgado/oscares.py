"""pretende-se que desenvolva um algoritmo para registar o nome de 10 filmes e as respetivas pontuações.
As pontuações são atribuídas numa escala de 0 a 20 pontos.
Estes dados devem ser armazenados em dois vectores (lista), um para o nome dos filmes e outro para as pontuações
(sendo a correspondência do nome do filme - pontuação efectuada pelo índice do vector (lista)).
Pode substituir os vetores anteriores com uma estrutura e uma vetor (lista).
"""

import os
def limpa():
    os.system('cls')

def cabecalho(texto):
    limpa()
    print(" "+ texto)

def introduzir_dados ():
    contador = len(lista_dados) + 1
    for i in range(1,11):
        print("Registe o nome do "+ str(contador)+ "º filme")
        nome_filme = input(" Nome: ")
        nota = int(input(" Nota (0 a 20): "))
        registo = [nome_filme, nota]
        lista_dados.append(registo)
        contador = contador + 1
        print()

def geracao_de_dados():

    print()
    print("Nome do filme           Classificação")
    print("="*47)
    contador = 1
    for elemento in lista_dados:
        nome = elemento[0]
        nota = elemento[1]
        print(contador, " "*(3-len(str(contador))), nome, " "*(20-len(str(nome))), nota)
        contador = contador + 1
    print()
    input("Enter para continuar.")

def alterar_dados():
    cabecalho("Alterar dados.")
    print()
    print("Nome               Classificação")
    print("="*47)
    conatdor = 1
    for elemento in lista_dados:
        nome = elemento[0]
        nota = elemento[1]
        print(contador, " " * (3 - len(str(contador))), nome, " " * (20 - len(str(nome))), nota)
        contador = contador + 1
    print()
    registo = int(input("Nº de registo a alterar:"))
    if registo > 0 and registo < contador:
            registo = registo - 1
            print()
            print(f"Nome:  {lista_dados[registo][0]}")
            print(f"Classificação: {lista_dados[registo][1]}")
            print()
            print("Alterar registo: ")
            novo_nome = input("Alterar nome: ")
            nova_nota = int(input("Alterar nota: "))
            lista_dados[registo][0] = novo_nome
            lista_dados[registo][1] = nova_nota
            print()
            print("Registo alterado! ")
            print("Enter para continuar.")

def eliminar_dados():
    cabecalho("Eliminar dados.")
    print()
    print("Nome               Classificação")
    print("=" * 47)
    contador = 1
    for elemento in lista_dados:
        nome = elemento[0]
        nota = elemento[1]
        print(contador, " " * (3 - len(str(contador))), nome, " " * (20 - len(str(nome))), nota)
        contador = contador + 1
    print()
    registo = int(input("Nº de registo a eliminar: "))
    if registo > 0 and registo < contador:
        registo = registo - 1
        print()
        print(f"Nome:  {lista_dados[registo][0]}")
        print(f"Classificação: {lista_dados[registo][1]}")
        lista_dados.pop(registo)
        print()
        print("Registo eliminado! ")
        print("Enter para continuar.")


def consultar():
    cabecalho("Consultar.")
    print()
    print("Nome               Classificação")
    print("=" * 47)
    contador = 1
    for elemento in lista_dados:
        nome = elemento[0]
        nota = elemento[1]
        print(contador, " " * (3 - len(str(contador))), nome, " " * (20 - len(str(nome))), nota)
        contador = contador + 1
    print()
    input("Enter para continuar. ")


def pesquisar():
    cabecalho("Pesquisar.")
    
    filme_procurar = input("Nome do filme a pesquisar: ")
    existe = False
    for i in range(len(lista_dados)):
        nome = lista_dados[i][0]

        if nome == filme_procurar:
            existe = True
            pos = i
    
    if existe == True:
        print(" Filme: ", lista_dados[pos][0])
        print(" Nota: ", lista_dados[pos][1])
    else:        
        print("Filme não exsite")

    print()
    input("Enter para continuar. ") 

def podio():
    cabecalho("Pódio.")
      # ordenar tabela
    lista_ordenada = sorted(lista_dados, key=lambda x: x[1], reverse=True)
    
    # mostrar os 3 primeiros
    print()
    print("Nome               Classificação")
    print("=" * 47)
    contador = 1
    for i in range(3):
        nome = lista_ordenada[i][0]
        nota = lista_ordenada[i][1]
        print(contador, " " * (3 - len(str(contador))), nome, " " * (20 - len(str(nome))), nota)
        contador = contador + 1
    print()


    input("Enter para continuar. ")
    

def guardar_ficheiro():  
    cabecalho("Guardar ficheiro.")
    #print(lista_dados)

    ficheiro = open("dados_filmes.txt","w", encoding="utf")
    ficheiro.write("nome; nota\n")
    for i in range(len(lista_dados)):
        ficheiro.write(f"{lista_dados[i][0]}; {lista_dados[i][1]}\n")

    ficheiro.close()
    print()
    print("Ficheiro guardado! ")
    input("Enter para continuar. ")

def carregar_dados_ficheiro():
    cabecalho("Carregar dados do ficheiro.")

    import pathlib
    fic = pathlib.Path("dados_filmes.txt")
  
    if fic.is_file():
        ficheiro = open("dados_filmes.txt","r", encoding="utf")

        # percorrer todo o ficheiro de texto
        contador = 1
        for linha in ficheiro.readlines():
            if contador > 1: # ignorar a 1ª linha
                lista_campos = linha.split(";") 
                registo = [lista_campos[0], int(lista_campos[1])]

                lista_dados.append(registo)

            contador = contador + 1

        print(lista_dados)
    
        print("Ficheiro aberto!")   
    else:
        print("Ficheiro não existe!")

   
    # pausa  
    input("Enter para continuar. ")

def main():
    global lista_dados
    lista_dados = []
    while True:
        cabecalho("Menu")
        print(" 1. Introduzir dados.")
        print(" 2. Geração de dados.")
        print(" 3. Alterar dados.")
        print(" 4. Eliminar dados.")
        print(" 5. Consultar.")
        print(" 6. Pesquisar (ver dados de um filme). ")
        print(" 7. Pódio.")
        print(" 8. Guardar em ficheiro.")
        print(" 9. Carregar dados do ficheiro.")
        print("10. Sair.")
        print()
        opcao = int(input("Escolha a opcao: "))

        if opcao == 1:
            introduzir_dados()
        elif opcao == 2:
            geracao_de_dados()
        elif opcao == 3:
            alterar_dados()
        elif opcao == 4:
            eliminar_dados()
        elif opcao == 5:
            consultar()
        elif opcao == 6:
            pesquisar()
        elif opcao == 7:
            podio()
        elif opcao == 8:
            guardar_ficheiro()
        elif opcao == 9:
            carregar_dados_ficheiro()
        elif opcao == 10:
            break
        else:
            print("Opção errada!")

main()
