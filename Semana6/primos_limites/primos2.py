def primos_ate(limite):
    lista = []
    for i in range(1, limite +1):
        contador = 0
        for j in range (1, i+1):
            if i % j == 0:
                contador += 1
        if contador == 2:
            lista += [i]
    return lista

assert primos_ate(10) == [2, 3, 5, 7]
assert primos_ate(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]