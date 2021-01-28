"""QII.

Faça um algoritmo em Python que leia um conjunto de 20 temperaturas em graus celsius 
(pode ter casas decimais). 
O algoritmo deve apresentar no ecrã a média das temperaturas, a temperatura máxima e 
temperatura mínima.
"""

soma = 0
max = min = 0

for i in range(20): # ciclo com i  de 0 a 19
    temp = float(input(str(i+1) + "ª temperatura: "))
    soma = soma + temp

    # considerar a 1ª temp max e min, para ter uma valor de referencia inicial
    if i == 0:
        max = temp
        min = temp

    if temp > max:
        max = temp
    
    if temp < min:
        min = temp

    # fim for

media = soma / 20
print(f"Media Temp:........: {media}")
# ou 
# print("Media temp...:", media)

print(f"Temp Máxima:.......: {max}")
print(f"Temp Minima:.......: {min}")


