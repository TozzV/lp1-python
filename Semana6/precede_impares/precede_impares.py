def precede_impares(numeros):
    lista = []
    for i in range(1, len(numeros)):
        if int(numeros[i-1]) % 2 == 0 and int(numeros[i]) % 2 != 0:
            if len(lista) >= 1:
                for h in range(len(lista)):
                    if numeros[i-1] == lista[h]:
                        break
                    elif numeros[i-1] != lista[h] and h == len(lista) -1:
                        lista += [numeros[i-1]]
            else:
                lista += [numeros[i-1]]
    return lista

assert precede_impares([15, 2, 4, 3, 8, 7, 6]) == [4, 8]
assert precede_impares([4, 3, 2, 2, 4, 5]) == [4]
assert precede_impares([1, 5, 4, 3, 8, 7]) == [4, 8]