def cabecalho(texto):
    print("=" * 30)
    print(" " + texto)
    print("=" * 30)


def introduzir_dados():
    cabecalho("INTRODUZIR DADOS")
    numero_livros = int(input("Introduza o numero de livros que pretende guardar informacao: "))
    for i in range(numero_livros):
        n_do_livro = int(input("Introduza o numero do livro: "))
        titulo_livro = input("Introduza o titulo do livro: ")
        autor = input("Introduza o nome do autor: ")
        categoria_do_livro = input("Introduz a categoria do livro: ")
        edicao = input("Introduza a edicao do livro: ")
        registo = [n_do_livro, titulo_livro, autor, categoria_do_livro, edicao]
        lista_dados.append(registo)


def alterar_dados():
    cabecalho("ALTERAR DADOS")
    print()
    print("#   Titulo    Autor      Categoria      Edicao             Numero")
    print("=" * 74)
    contador = 1
    for elemento in lista_dados:
        n_do_livro = elemento[0]
        titulo_livro = elemento[1]
        autor = elemento[2]
        categoria_do_livro = elemento[3]
        edicao = elemento[4]

        print(contador, " " * (2 - len(str(contador))), titulo_livro, " " * (7 - len(str(titulo_livro))), autor," " * (14 - len(str(autor))), categoria_do_livro, " " * (13 - len(str(categoria_do_livro))), edicao," " * (17 - len(str(edicao))), n_do_livro)

        contador = contador + 1

    print()
    registo = int(input("Nº Registo a alterar (#): "))

    if registo > 0 and registo < contador:
        registo = registo - 1
        print()
        print(f"Numero.....: {lista_dados[registo][0]}")
        print(f"Titulo.......: {lista_dados[registo][1]}")
        print(f"Autor.......: {lista_dados[registo][2]}")
        print(f"Categoria.......: {lista_dados[registo][3]}")
        print(f"Edicao.......: {lista_dados[registo][4]}")

        print()
        print("Alterar registo:")
        novo_numero = int(input("Alterar numero do livro..........: "))
        novo_titulo = input("Alterar o titulo do livro........: ")
        novo_autor = input("Alterar o autor do livro.........: ")
        nova_categoria = input("Alterar a categoria do livro.....: ")
        nova_edicao = input("Alternar a edicao do livro.......: ")

        lista_dados[registo][0] = novo_numero
        lista_dados[registo][1] = novo_titulo
        lista_dados[registo][2] = novo_autor
        lista_dados[registo][3] = nova_categoria
        lista_dados[registo][4] = nova_edicao

        print()
        print("Registo alterado!")


def eliminar_dados():
    cabecalho("ELIMINAR DADOS")
    print()
    print("#   Titulo    Autor      Categoria      Edicao            Numero")
    print("=" * 74)
    contador = 1
    for elemento in lista_dados:
        n_do_livro = elemento[0]
        titulo_livro = elemento[1]
        autor = elemento[2]
        categoria_do_livro = elemento[3]
        edicao = elemento[4]

        print(contador, " " * (2 - len(str(contador))), titulo_livro, " " * (7 - len(str(titulo_livro))), autor," " * (14 - len(str(autor))), categoria_do_livro, " " * (13 - len(str(categoria_do_livro))), edicao," " * (17 - len(str(edicao))), n_do_livro)

        contador = contador + 1
    print()
    registo = int(input("N registo a eliminar (#): "))

    if registo > 0 and registo < contador:
        registo = registo - 1
        print()
        print(f"Numero.....: {lista_dados[registo][0]}")
        print(f"Titulo.......: {lista_dados[registo][1]}")
        print(f"Autor.......: {lista_dados[registo][2]}")
        print(f"Categoria.......: {lista_dados[registo][3]}")
        print(f"Edicao.......: {lista_dados[registo][4]}")
        lista_dados.pop(registo)
        print()
        print("Registo eliminado!")

def consultar():
    cabecalho("CONSULTAR")
    print()
    print("#   Titulo    Autor      Categoria      Edicao            Numero")
    print("=" * 74)
    contador = 1
    for elemento in lista_dados:
        n_do_livro = elemento[0]
        titulo_livro = elemento[1]
        autor = elemento[2]
        categoria_do_livro = elemento[3]
        edicao = elemento[4]

        print(contador, " " * (2 - len(str(contador))), titulo_livro, " " * (7 - len(str(titulo_livro))), autor," " * (14 - len(str(autor))), categoria_do_livro, " " * (13 - len(str(categoria_do_livro))), edicao," " * (17 - len(str(edicao))), n_do_livro)

        contador = contador + 1

    print()
    input("ENTER p/ continuar....")



def guardar():
    cabecalho("GUARDAR")

    ficheiro = open("dados_livros", "w")
    ficheiro.write("titulo; autor; categoria; edicao; numero")

    for i in range(len(lista_dados)):
        ficheiro.write(f"{lista_dados[i][0]}; {lista_dados[i][1]}; {lista_dados[i][2]}; {lista_dados[i][3]}; {lista_dados[i][4]}\n")

    ficheiro.close()
    print()
    print("Ficheiro Guardado!")



def main():

    global lista_dados
    lista_dados = []


    while True:
        cabecalho("MENU")
        print(" 1. Introduzir dados")
        print(" 2. Alterar dados")
        print(" 3. Eliminar dados")
        print(" 4. Consultar")
        print(" 5. Guardar")
        print(" 6. Sair")
        print()
        opcao = int(input("Escolha a opcao: "))

        if opcao == 1:
            introduzir_dados()
        elif opcao == 2:
            alterar_dados()
        elif opcao == 3:
            eliminar_dados()
        elif opcao == 4:
            consultar()
        elif opcao == 5:
            guardar()
        elif opcao == 6:
            break
        else:
            print("Opcao errada!")
main()