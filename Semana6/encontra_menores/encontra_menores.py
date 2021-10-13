def encontra_menores(num, lista):
    contador = 0
    for i in range(len(lista)):
        if lista[i] >= num:
            contador += 1
        elif num > lista[i]:
            return lista[i]
            break
    if contador > 0:
        return -1
            
lista1 = [100,200,300,400]
lista2 = [15, 12, 4, 9, 10]
