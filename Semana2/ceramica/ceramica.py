# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Caixas de Cerâmica
# Objetivo do código: Calcular a área total a revestir e quantas caixas de cerâmica serão necessárias

capacidade_revestimento = float(input())

comprimento = float(input())
largura = float(input())
altura = float(input())

area_parede1 = largura * altura
area_parede2 = comprimento * altura
area_chao = comprimento * largura


area_total = area_chao + ( (area_parede1 * 2)  + (area_parede2 * 2))
numero_caixas = float(area_total / capacidade_revestimento)

print(f'Capacidade de revestimento? ')
print('== Dados do vão a revestir ==')
print(f'Comprimento? Largura? Altura? ')
print('== Resultados ==')
print(f'Área total a revestir: {area_total} m2')
print(f'Número de caixas: {int(numero_caixas)}')

