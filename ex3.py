def min_max(lista):
    if not lista:
        return None
    
    minimo = maximo = lista[0]

    for numero in lista:
        if numero < minimo:
            minimo = numero
        elif numero > maximo:
            maximo = numero

    return (minimo, maximo)

numeros = []
while True:
    numero = int(input('Informe um número(0 para parar): '))
    if numero != 0:
        numeros.append(numero)
    else:
        break
minimo, maximo = min_max(numeros)

print(f"O número mínimo na lista é: {minimo}")
print(f"O número máximo na lista é: {maximo}")