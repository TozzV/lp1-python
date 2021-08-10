# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Ano bissexto
# Objetivo do código: Descobrir se um ano é bissexto

ano = int(input())

if ano % 4 == 0:
    if ano % 400 == ano % 100:
        print(f'{ano} é bissexto')
    else: 
        print(f'{ano} não é bissexto')
else:
    print(f'{ano} não é bissexto')  