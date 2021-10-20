# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Elimina Menores
# Objetivo do código: remover os valores menores de uma lista a partir de um valor 
# informado e retornar a quantidade de remoções,

def elimina_menores(num, lista):
    contador = 0    
    while len(lista) > 1:
        x = True
        for i in range(len(lista)):
            if lista[i] < num:
                lista.pop(i)
                contador += 1
                break
            elif i == (len(lista)-1):
                x = False
        if x == False:
            break
    return contador


