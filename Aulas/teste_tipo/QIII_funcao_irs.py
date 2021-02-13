"""QIII.

Construa uma função (calcula_irs) (Python) que receba como parâmetro um valor em euros e 
calcule o valor do IRS de acordo com as seguintes condições:

-Se valor euros menor que 1000 então IRS é 10%
-Se valor euros maior de 1000 e inferior a 1500 então IRS é 20%
-Se valor euros maior de 1500 então IRS é 30%

Exemplo de chamada da função:
valor_euros = float(input("Salário: ")
valor_IRS = calcula_irs(valor_euros) ou.. valor_IRS = calcula_irs(1500)
print(f“Valor IRS:: {valor_IRS}”)

Apresente também o programa principal (procedimento), com respetiva chamada 
da função e escrita da informação pedida.
"""

def calcula_irs(valor_salario):

    if valor_salario < 1000:
        valor_irs = valor_salario * 10 / 100
    elif valor_salario < 1500:
        valor_irs = valor_salario * 20 / 100
    else:
        valor_irs = valor_salario * 30 / 100

    return valor_irs    

def main():
    salario = float(input("Salário.: "))
    irs = calcula_irs(salario)
    
    print(f"Valor IRS..: {irs}")

main()