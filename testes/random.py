# Importar a biblioteca random para geração de número aleatório

import random

# gerar número aleatório entre 1 e 49
for i in range(5):
    numero_aleatorio = random.randint(1, 49)
    print(numero_aleatorio)


# selecionar as Letras A, B, C, D

numero_aleatorio = random.randint(1, 4)
if numero_aleatorio == 1:
    letra = "A"
elif numero_aleatorio == 2:
    letra = "B"
elif numero_aleatorio == 3:
    letra = "C"
else:
    letra = "D"

# print(letra)

for i in range(5):
    letras = ["A", "B", "C", "D", "E"]
    indice = random.randint(0, len(letras)-1)
    print(letras[indice])




