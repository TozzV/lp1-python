# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Ritmo Maratonista
# Objetivo do código: Calcular o ritmo de um maratonista a parti da
# quantidade de kilometros percorridos e seu tempo


kilometros_percorridos = float(input())
tempo_demorado = float(input())

ritmo = tempo_demorado / kilometros_percorridos

print(f'O ritmo do maratonista foi {ritmo:.2f} min/km.')