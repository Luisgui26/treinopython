def numeros_pares(lista):
    numeros_pares = []
    for numero in lista:
        if numero % 2 == 0:
            numeros_pares.append(numero)
    return numeros_pares

numeros = []

while True:
    numero = int(input('Informe um número(0 para sair): '))
    if numero != 0:
        numeros.append(numero)
    else:
        break
pares = numeros_pares(numeros)
print(f'Os pares são: {pares}')