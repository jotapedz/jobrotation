def fibonacci(n):
    #Inicializa a sequência com os valores iniciais
    sequencia = [0, 1]
    while len(sequencia) < n:
        # Calcula o próximo termo da sequência como a soma dos dois termos anteriores
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
    return sequencia

#Lê o número informado 
num = int(input('Informe um número: '))

#Calcula a sequência de Fibonacci até o número informado
seq_fib = fibonacci(num)

#Verifica se o número informado pertence a sequência de Fibonacci
if num in seq_fib:
    print(f'O número {num} pertence à sequência de Fibonacci: {seq_fib}')
else:
    print(f'O número {num} não pertence à sequência de Fibonacci: {seq_fib}')