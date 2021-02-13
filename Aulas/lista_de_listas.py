letras_num = [["A", 100], ["B", 200], ["C", 300], ["D", 400]]

print(letras_num)

#aceder ao item 2 da lista -> ["B", 200]
print(letras_num[1])  # -> ["B", 200] 

#aceder ao item 1 (200) do item 2 da lista ["B", 200]

print(letras_num[1][1]) #  - [200]

#adicianr o item à lista ["E", 500]
letras_num.append(["E", 500])
print(letras_num)

# letras_num = []
# perguntar ao utilizado os dados do item
l = input("Letra: ")
n = int(input("Numero: "))

#registo = [l, n]
#letras_num.append(registo)
#ou ..
letras_num.append([l, n])

print(letras_num)

# percorrer toda a lista através do indice
tam = len(letras_num)
for i in range(tam): # i de 0 a tam-1
    print(letras_num[i][0], " - ", letras_num[i][1] )

# percorrer toda a lista através de cada item
for item in letras_num:
     print(item[0], " - ", item[1] )     

# colocar todos os valores os a zero, exemplo ["A", 0], ["B", 0]
# percorrer toda a lista através do indice
tam = len(letras_num)
for i in range(tam): # i de 0 a tam-1
    letras_num[i][1] = 0

print(letras_num)


