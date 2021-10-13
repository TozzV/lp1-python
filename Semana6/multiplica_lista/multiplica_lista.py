l = ['joao', 'pedro']
n = 0

def multiplica_lista(n,lista):
    resultado = []
    for i in range(n):
        resultado += lista
    return resultado
        

assert multiplica_lista(2,l) == ['joao', 'pedro', 'joao', 'pedro']
assert multiplica_lista(0,l) == []
