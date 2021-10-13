# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Seleciona Sequências
# Objetivo do código: Informa sequências que são menores que o valor do fator informado

fator = input()
lista = []
contador = 0

while(True):
    sequencia = input()
    if sequencia == 'fim':
        break
    x = sequencia.split(" ")
    lista.append(x)

for i in range(len(lista)):
    contador = 0 
    for j in range(len(lista[i])):
        if int(lista[i][j]) > int(fator):
            contador +=1  
    if contador > (len(lista[i]) / 2):
        print(f'Sequência {i+1}:', end='')
        for k in range(len(lista[i])):
            print(f' {lista[i][k]}', end='')
        print()