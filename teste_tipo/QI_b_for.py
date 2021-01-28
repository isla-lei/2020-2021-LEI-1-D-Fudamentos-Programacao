"""QI_b.

Algoritmo que implementa um ciclo que pede 20 números (que representam temperaturas)
ao utilizador e faz a contagem das temperaturas negativas (<0) e positivas,
apresentado no final esses valores
"""

# for i in range(20): # ciclo com i de 0 a 19

conta_negativas = 0
conta_positivas = 0
for i in range(1, 21): # ciclo com i de 1 a 20
    # print(i)
    temp = float(input("Temperatura " + str(i) + ": "))
    if temp < 0:
        conta_negativas = conta_negativas + 1
    else:
        conta_positivas = conta_positivas + 1
    
print(f"Temperaturas positivas: {conta_positivas}")
print(f"Temperaturas negativas: {conta_negativas}")

