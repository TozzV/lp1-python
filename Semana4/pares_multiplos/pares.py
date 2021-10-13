sequencia = input().split()
fator = int(input())

contador = 0 
pares = []

for i in range(len(sequencia) - 1):
    if int(sequencia[i]) * fator == int(sequencia[i+1]) or int(sequencia[i+1]) * fator == int(sequencia[i]):
        contador += 1
        pares.append(f'{sequencia[i]} {sequencia[i+1]}')
    
print(f'{contador} par(es)')

for j in pares:
    print(j)
