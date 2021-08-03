# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Elevador
# Objetivo do código: calcular a capacidade de um 
# elevador a partir do número de pessoas

capacidade = int(input())
pessoas = int(input())

media_pessoas = int(capacidade / pessoas)

print(f'O elevador pode transportar {media_pessoas} pessoas com segurança.')