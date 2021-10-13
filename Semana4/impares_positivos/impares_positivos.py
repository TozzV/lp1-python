sequencia = input().split(" ")

contador = 0

maior = 0 
menor = 0
soma = 0 

for i  in range(len(sequencia)):
    if int(sequencia[i]) % 2 != 0:
        contador += 1
        soma += int(sequencia[i])    
        if int(sequencia[i]) > maior:
            maior = int(sequencia[i])
        if int(sequencia[i]) < menor:
            menor = int(sequencia[i])
        if maior == 0 or menor == 0:
            maior, menor = int(sequencia[i]), int(sequencia[i])

print('Resumo dos Ímpares Positivos')
print("")
if contador == 0:
    print(f'Quantidade: {contador}')
    print(f'Soma: {soma}')
    print('Maior: Não existe')
    print('Menor: Não existe')

else:
    print(f'Quantidade: {contador}')
    print(f'Soma: {soma}')
    print(f'Maior: {maior}')
    print(f'Menor: {menor}')
