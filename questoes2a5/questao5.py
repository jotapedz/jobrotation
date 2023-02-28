#String a ser invertida
string = "abcdefg"

#Converte a string em uma lista de caracteres
lista = list(string)

#Inverte a lista
for i in range(len(lista) // 2):
    j = len(lista) - i - 1
    lista[i], lista[j] = lista[j], lista[i]

#Converte a lista de volta para uma string
stringinve = ''.join(lista)

#Imprime a string invertida
print(stringinve)
