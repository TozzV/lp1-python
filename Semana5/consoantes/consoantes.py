contador = 0
contadorConsoante = 0
vogais = ['a','A','e','E','i','I','o','O','u','U']


while (True):
    palavra = input()
    if palavra == '***':
        break
    if palavra[0] in vogais:
        contador += 1
    else:
        contadorConsoante += 1

print(f'Palavras: {contadorConsoante}')