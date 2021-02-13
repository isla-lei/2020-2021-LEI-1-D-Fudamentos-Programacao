import os

def limpa_ecra():
    os.system("cls")

def cabecalho(texto):
    limpa_ecra()
    print("=" * 25)
    print(texto)
    print("=" * 25)

def inscrever_jogador():
    cabecalho("INSCREVER JOGADOR(ES)")
    contador = len(lista_dados) + 1
    while True:
        print("Registo Nº ", contador)
        numero = int(input(" Número (0 p/terminar): "))
        if numero == 0:
            break
        nome = input(" Nome.................: ")
        valor_mercado = float(input(" Valor de Mercado.................: "))
        registo = [numero, nome, valor_mercado]
        lista_dados.append(registo)
        contador = contador + 1

def consultar_jogador():
    cabecalho("CONSULTAR JOGADOR(ES)")
    print("#     Número      Nome                            Valor de Mercado")
    print("------------------------------------------------------------------")
    n = len(lista_dados)
    for i in range(n):
        numero = lista_dados[i][0]
        nome = lista_dados[i][1]
        valor_mercado = lista_dados[i][2]
        print((i + 1), " " * (4 - len(str(i))), numero, " " * (10 - len(str(numero))), nome, " " * (30 - len(nome)), valor_mercado)
    print()
    input("ENTER p/ terminar...")

def mostrar_mediavalormercado():
    cabecalho("MÉDIA VALOR DE MERCADO")
    n = len(lista_dados)
    soma = 0
    for i in range(n):
        soma = soma + lista_dados[i][2]
    if n > 0:
        media = soma / n
        print(F"Média Valor de Mercado: {media}")
    else:
        print("Sem dados....")
    print()
    input("ENTER p/ terminar...")

def mostrar_maximovalormercado():
    cabecalho("VALOR DE MERCADO MAIS ELEVADO")
    n = len(lista_dados)
    if n > 0:
        max = lista_dados[0][2]
        posicao = 0
    else:
        print("Sem dados....")
    for i in range(n):
        if lista_dados[i][2] > max:
            max = lista_dados[i][2]
            posicao = i
    print()
    if n > 0:
        print(f"Valor de Mercado mais elevado...: {max}")
        print(f"Número......: {lista_dados[posicao][0]}")
        print(f"Nome........: {lista_dados[posicao][1]}")
        print(f"Valor de Mercado........: {lista_dados[posicao][2]}")
    print()
    input("ENTER p/ terminar...")

def guardar_ficheiro():
    cabecalho("GUARDAR FICHEIRO")
    ficheiro = open("dados_jogador(es).txt", "w", encoding='utf8')
    ficheiro.write("Número, Nome, Valor de Mercado\n")
    for item in lista_dados:
        ficheiro.write(str(item[0]) + ", " + item[1] + ", " + str(item[2]) + "\n")
    ficheiro.close()
    print()
    print("Ficheiro guardado!")
    input("ENTER p/ terminar...")

def abrir_ficheiro():
    cabecalho("ABRIR FICHEIRO")
    ficheiro = open("dados_jogador(es).txt", "r", encoding='utf8')
    contador = 1
    for linha in ficheiro.readlines():
        if contador > 1:
            lista_campos = linha.split(",")
            registo = [int(lista_campos[0]), lista_campos[1].strip(), float(lista_campos[2])]
            lista_dados.append(registo)
        contador = contador + 1
    print(lista_dados)
    print()
    print("Ficheiro aberto!")
    input("ENTER p/ terminar...")

def alterar_dados():
    cabecalho("ALTERAR DADOS")
    print()
    n = len(lista_dados)
    for i in range(n):
        registo = int(input("Nº Registo a alterar (#).: "))
        if registo == 0:
            break
        if registo > 0 and registo < n:
            registo = registo - 1
            print()
            print(f"Número.....: {lista_dados[registo][0]}")
            print(f"Nome.......: {lista_dados[registo][1]}")
            print(f"Valor de Mercado.......: {lista_dados[registo][2]}")
            print()
            print("Alterar registo:")
            novo_nome = input(" Alterar nome...............: ")
            novo_valormercado = float(input(" Alterar valor de mercado...............: "))
            lista_dados[registo][1] = novo_nome
            lista_dados[registo][2] = novo_valormercado
            print()
            print("Registo alterado!")
            input("ENTER p/ continuar....")

def eliminar_dados():
    cabecalho("ELIMINAR DADOS")
    print()
    print("#     Número      Nome                            Valor de Mercado")
    print("------------------------------------------------------------------")
    contador = 1
    for elemento in lista_dados:
        numero = elemento[0]
        nome = elemento[1]
        valor_mercado = elemento[2]
        print(contador, " " * (3 - len(str(contador))), numero, " " * (8 - len(str(numero))), nome, " " * (30 - len(str(nome))), valor_mercado)
        contador = contador + 1
    print()
    registo = int(input("Nº Registo a eliminar (#).: "))
    if registo > 0 and registo < contador:
        registo = registo - 1
        print()
        print(f"Número.....: {lista_dados[registo][0]}")
        print(f"Nome.......: {lista_dados[registo][1]}")
        print(f"Valor de  Mercado.......: {lista_dados[registo][2]}")
        lista_dados.pop(registo)
        print()
        print("Registo eiminado!")
        input("ENTER p/ continuar....")

def main():
    global lista_dados
    lista_dados = []
    while True:
        cabecalho("LIGA PORTUGAL")
        print(" 1. INSCREVER JOGADOR(ES)")
        print(" 2. CONSULTAR JOGADOR(ES)")
        print(" 3. MÉDIA VALOR DE MERCADO")
        print(" 4. VALOR DE MERCADO MAIS ELEVADO")
        print(" 5. GUARDAR FICHEIRO")
        print(" 6. ABRIR FICHEIRO")
        print(" 7. ALTERAR DADOS")
        print(" 8. ELIMINAR DADOS")
        print(" 9. SAIR")
        print()
        opcao = int(input(" Escolha a opção: "))
        if opcao == 1:
            inscrever_jogador()
        elif opcao == 2:
            consultar_jogador()
        elif opcao == 3:
            mostrar_mediavalormercado()
        elif opcao == 4:
            mostrar_maximovalormercado()
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
            print("Opção Errada!")
if __name__ == "__main__":
    main()