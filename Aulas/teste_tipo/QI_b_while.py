"""QI_b.

Algoritmo que implementa um ciclo que pede 20 números (que representam temperaturas)
ao utilizador e faz a contagem das temperaturas negativas (<0) e positivas,
apresentado no final esses valores
"""
conta_negativas = 0
conta_positivas = 0
i = 1
while i <= 20:
    # print(i)
    temp = float(input("Temperatura " + str(i) + ": "))
    if temp < 0:
        conta_negativas = conta_negativas + 1
    else:
        conta_positivas = conta_positivas + 1
        
    i = i + 1

print(f"Temperaturas positivas: {conta_positivas}")
print(f"Temperaturas negativas: {conta_negativas}")

