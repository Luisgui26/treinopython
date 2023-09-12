def maior_palavra(lista):
    if not lista:
        return None

    palavra_longa = lista[0]

    for palavra in lista:
        if len(palavra) > len(palavra_longa):
            palavra_longa = palavra
        
    return palavra_longa

lista = []
while True:
    palavra = input('Informe uma palavra(digite piu para parar): ')
    if palavra != 'piu':
        lista.append(palavra)
    else:
        break
palavra_longa = maior_palavra(lista)
print(f'A maior palavra é: {palavra_longa}')


