# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Quadrado da circuferência
# Objetivo do código: calcular a  área de um quadrado inscrito em um circulo


import math;

raio = float(input())

area_circulo = math.pi * (raio ** 2)
area_quadrado = (raio ** 2) * 2
diferença_tamanho = area_circulo - area_quadrado

print(f'Área não comum: {diferença_tamanho:.5f}')
