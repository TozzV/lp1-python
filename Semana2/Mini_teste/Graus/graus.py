# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Graus para radianos
# Objetivo do código: transformar o valor de graus em radianos

import math; 

graus = float(input())

conversao = (math.pi / 180) * graus

print(f'{conversao:.3f}')