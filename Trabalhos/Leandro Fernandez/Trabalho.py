def cabecalho(texto):
    print("="*30)
    print(" " + texto)
    print("="*30)

def ler_dados():
    cabecalho("LER DADOS")
    numero_livros = int(input("Introduza o numero de livros que pretende guardar informação: "))
    for i in range(numero_livros):
        numero_do_livro = str(input("Introduza o número do livro: "))
        titulo_livro = input("Introduza o titulo do livro nº"+numero_do_livro+": ")
        autor = input("Introduza o autor do livro nº"+numero_do_livro+": ")
        categoria_livro = input("Introduza a categoria do livro nº"+numero_do_livro+": ")
        edicao = input("Introduza a edição do livro nº"+numero_do_livro+": ")
        numero_pag = input("Introduza o numero de paginas do livro nº"+numero_do_livro+": ")
        registo = [numero_do_livro,titulo_livro,autor,categoria_livro,edicao,numero_pag]
        lista_dados.append(registo)

def consultar():
    cabecalho("Consultar")
    print()
    print("#   Numero   Titulo          Autor          Categoria          Edição   Numero de Paginas")
    print("="*89)
    contador = 1
    for elemento in lista_dados:
        numero_do_livro = elemento[0]
        titulo_livro = elemento[1]
        autor = elemento[2]
        categoria_livro = elemento[3]
        edicao = elemento[4]
        numero_pag = elemento[5]

        print(contador, " "*(2-len(str(contador))), numero_do_livro, " "*(7-len(str(numero_do_livro))) , titulo_livro, " "*(14-len(str(titulo_livro))), autor, " "*(13-len(str(autor))), categoria_livro, " "*(17-len(str(categoria_livro))), edicao, " "*(7-len(str(edicao))), numero_pag)

        contador = contador + 1        
        
def alterar_dados():
    cabecalho("ALTERAR DADOS") 
    # mostra dados
    print()
    print("#   Numero   Titulo          Autor          Categoria          Edição   Numero de Paginas")
    print("="*89)
    contador = 1
    for elemento in lista_dados:
        numero_do_livro = elemento[0]
        titulo_livro = elemento[1]
        autor = elemento[2]
        categoria_livro = elemento[3]
        edicao = elemento[4]
        numero_pag = elemento[5]

        print(contador, " "*(2-len(str(contador))), numero_do_livro, " "*(7-len(str(numero_do_livro))) , titulo_livro, " "*(14-len(str(titulo_livro))), autor, " "*(13-len(str(autor))), categoria_livro, " "*(17-len(str(categoria_livro))), edicao, " "*(7-len(str(edicao))), numero_pag)

        contador = contador + 1
    print()
    registo = int(input("Nº Registo a alterar (#): "))
    if registo > 0 and registo < contador:
        # mostra registo
        registo = registo -1
        print()
        print(f"Numero.....: {lista_dados[registo][0]}")
        print(f"Titulo.......: {lista_dados[registo][1]}")
        print(f"Autor.......: {lista_dados[registo][2]}")
        print(f"Categoria.......: {lista_dados[registo][3]}")
        print(f"Edicao.......: {lista_dados[registo][4]}")
        print(f"Numero paginas.......: {lista_dados[registo][5]}")

        print()
        print("Alterar registo:")
        novo_numero = int(input("Alterar numero do livro..........: "))
        novo_titulo = input("Alterar o titulo do livro........: ")
        novo_autor = input("Alterar o autor do livro.........: ")
        nova_categoria = input("Alterar a categoria do livro.....: ")
        nova_edicao = input("Alternar a edicao do livro.......: ")
        novo_numero_pag = int(input("Alterar o numero de paginas......: "))
        # alterar registo
        lista_dados[registo][0] = novo_numero
        lista_dados[registo][1] = novo_titulo
        lista_dados[registo][2] = novo_autor
        lista_dados[registo][3] = nova_categoria
        lista_dados[registo][4] = nova_edicao
        lista_dados[registo][5] = novo_numero_pag

        print()
        print("Registo alterado!")


def eliminar_dados():
    cabecalho("ELIMINAR DADOS")
    print()
    print("#   Numero   Titulo          Autor          Categoria          Edição   Numero de Paginas")
    print("="*89)
    contador = 1
    for elemento in lista_dados:
        numero_do_livro = elemento[0]
        titulo_livro = elemento[1]
        autor = elemento[2]
        categoria_livro = elemento[3]
        edicao = elemento[4]
        numero_pag = elemento[5]

        print(contador, " "*(2-len(str(contador))), numero_do_livro, " "*(7-len(str(numero_do_livro))) , titulo_livro, " "*(14-len(str(titulo_livro))), autor, " "*(13-len(str(autor))), categoria_livro, " "*(17-len(str(categoria_livro))), edicao, " "*(7-len(str(edicao))), numero_pag)

        contador = contador + 1
    print()
    registo = int(input("Nº Registo a eliminar (#): "))

    if registo > 0 and registo < contador:
        # mostra registo
        registo = registo -1
        print()
        print(f"Numero.....: {lista_dados[registo][0]}")
        print(f"Nome.......: {lista_dados[registo][1]}")
        print(f"Nota.......: {lista_dados[registo][2]}")
        print(f"Nota.......: {lista_dados[registo][3]}")
        print(f"Nota.......: {lista_dados[registo][4]}")
        print(f"Nota.......: {lista_dados[registo][5]}")
        lista_dados.pop(registo)
        print()
        print("Registo eiminado!")

def guardar_em_ficheiro():
    cabecalho("GUARDAR EM FICHEIRO")
    ficheiro = open("dados_livros.txt","w")
    ficheiro.write("numero_do_livro; titulo_livro; autor; categoria_livro; edicao; numero_pag\n")

    for i in range(len(lista_dados)):
        ficheiro.write(f"{lista_dados[i][0]}; {lista_dados[i][1]}; {lista_dados[i][2]}; {lista_dados[i][3]}; {lista_dados[i][4]}; {lista_dados[i][5]}\n")
    
    ficheiro.close() 
    print()
    print("Ficheiro guardado!")
            

def carregar_dados_do_ficheiro():
    cabecalho("CARREGAR DADOS DO FICHEIRO")
    ficheiro = open("dados_livros.txt","r")
    print()
    contador = 1
    for linha in ficheiro.readlines():
        if (contador > 1):
            campos = linha.split(";")
            registo = [str(campos[0]), campos[1].lstrip(), campos[2].lstrip(), campos[3].lstrip(), campos[4].lstrip(), campos[5].lstrip("\n")]
            lista_dados.append(registo)

        contador = contador + 1

    print(lista_dados)
    print()
    print("Ficheiro aberto!")
    print()



def main():
    
    global lista_dados
    lista_dados = []
    
    while True:
        print("="*30)
        print("MENU")
        print("="*30)
        print(" 1. Introduzir dados do/s livro")
        print(" 2. Consultar dados")
        print(" 3. Eliminar dados")
        print(" 4. Alterar dados")
        print(" 5. Guardar em ficheiro")
        print(" 6. Carregar dados do ficheiro")
        print(" 7. Sair")
        print()
        opcao = int(input("Escolha a opcao: "))

        if opcao == 1:
            ler_dados()
        elif opcao == 2:
            consultar()
        elif opcao == 3:
            eliminar_dados()
        elif opcao == 4:
            alterar_dados()
        elif opcao == 5:
            guardar_em_ficheiro()
        elif opcao == 6:
            carregar_dados_do_ficheiro()
        elif opcao == 7:
            break
        else:
            print("Opção errada!")
main() 
      






   



    

    





