# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Diagonais
# Objetivo do código: calcular o número de diagonais de um poligono

numero_lados = int(input())

formula_poligono = ( numero_lados / 2 ) * ( numero_lados - 3)

print(f'{numero_lados} lados => {int(formula_poligono)} diagonais')