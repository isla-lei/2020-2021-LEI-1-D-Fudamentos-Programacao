"""

Elabore um programa em Python que leia um número N entre 1 e 12, 
correspondente ao n.º de meses que um determinado vendedor trabalhou. 
Obs: deve validar o N para permitir apenas valores entre 1 e 12.

Em seguida, deve ler N valores em euros correspondentes às vendas efetuadas em 
cada mês, para uma lista vendas_anual
"""

#def  mes_maior_vendas(num_meses, vendas_anual):


def main():

    # repetir a pergunta (infinitamente) até o num_meses estar entre 1 e 12

    while True:
        num_meses = int(input("Nº de meses que trabalhou (1..12)..:"))
        if num_meses < 1 or num_meses > 12:
            print("Nº de meses errado! deve ser entre 1 e 12")

        # condicao de terminar o ciclo (while True), quando num_meses está entre 1 e 12
        if num_meses > 0 and num_meses < 13:
            break # termina o ciclo

        # fim while

    # ler os dados de cada mês
    # declarar a lista -> colecao de dados
    lista_vendas_anual = []

    for i in range(num_meses): # i de 0 a num_mes-1
        valor_venda = float(input(" Valor do mês " + str(i+1) + ": "))
        lista_vendas_anual.append(valor_venda)

    print(lista_vendas_anual)

    # chamar as funcoes
    #mes_maior = mes_maior_vendas(num_meses, lista_vendas_anual)
    #print(mes_maior)


main()