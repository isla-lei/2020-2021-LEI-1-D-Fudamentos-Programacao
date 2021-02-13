# guardar dados de funcionarios com os campos (numero, nome, salario, IRS, seg_social)
# 2 abordagens
# 1ª - 5 listas
lista_numeros = []
lista_nomes = []
lista_salarios = []
lista_irs = []
lista_ss = []

# pedir 2 func
for i in range(2):
    numero = int(input("Numero: "))
    lista_numeros.append(numero)

    nome = input("Nome: ")
    lista_nomes.append(nome)

    salario = float(input("Salario: "))
    lista_salarios.append(salario)

    irs = salario * 20 / 100
    print("IRS: ", irs)
    lista_irs.append(irs)

    ss = salario * 11 / 100
    print("SS: ", ss)
    lista_ss.append(ss)

    print(lista_numeros)
    print(lista_nomes)
    print(lista_salarios)
    print(lista_irs)
    print(lista_ss)


    # 2ª - lista de listas
    # Vamos ter uma lista lista_dados, onde em cada célula deve ter os campos (numero, nome, salario, IRS, seg_social)
    # Exemplo da lista com 2 funcionários:
    # [[100, 'Nome 1', 1500, 300.0, 165.0], [200, 'Nome 2', 1000, 200.0, 110.0]]

    lista_funcionarios = []

    numero = int(input("Numero: "))
    nome = input("Nome: ")
    salario = float(input("Salario: "))
    irs = salario * 20 / 100
    print("IRS: ", irs)
    ss = salario * 11 / 100
    print("SS: ", ss)

    registo = [numero, nome, salario, irs, ss]
    lista_funcionarios.append(registo)
    # ou ..
    # lista_funcionarios.append([numero, nome, salario, irs, ss])
    print(lista_funcionarios)