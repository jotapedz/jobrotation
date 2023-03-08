# Definindo a string que será invertida
string = "Hello World!"

# Criando uma lista vazia para armazenar os caracteres invertidos
string_invertida = []

# Percorrendo a string de trás para frente e adicionando cada caractere na lista de caracteres invertidos
for i in range(len(string)-1, -1, -1):
    string_invertida.append(string[i])

# Transformando a lista de caracteres invertidos em uma string
string_invertida = ''.join(string_invertida)

# Imprimindo a string invertida.
print(string_invertida)
