# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Campos de Futebol
# Objetivo do código: Realizar o cálculo da medida em campos de futebol de acordo com a área. 
# Também informar qual a média das medidas.

area1 = float(input())
area2 = float(input())
area3 = float(input())

campos1 = area1  / 4000
campos2 = area2 / 4000
campos3 = area3 / 4000

print(f'{campos1:.2f}')
print(f'{campos2:.2f}')
print(f'{campos3:.2f}')

media = (campos1 + campos2 + campos3) / 3

print(f'{media:.2f}')