# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Área do cilindro 
# Objetivo do código: 

diametro = float(input())
altura = float(input())

raio = diametro / 2 
area_base = 3.141592653589793 * ( raio ** 2 )

perimetro_base = (3.141592653589793 * 2) * raio
area_lateral_cilindro = altura * perimetro_base 

area_cilindro = (area_base * 2) + area_lateral_cilindro

print("Cálculo da Superfície de um Cilindro")
print("---")
print(f'Medida do diâmetro? {diametro:.1f}')
print(f'Medida da altura? {altura:.1f}')
print("---")
print(f'Área calculada: {area_cilindro:.2f}')