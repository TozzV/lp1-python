# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Hipotenusa
# Objetivo do código: Realizar o cálculo de hipotenusa de um triângulo retângulo utilizando 
# os catetos,

Cateto1 = float(input("Medida do Cateto 1? "))
Cateto2 = float(input("Medida do Cateto 2? "))

Medida_da_Hipotenusa =  ((Cateto1 ** 2) + (Cateto2 ** 2)) ** (1 / 2)

print(f'Medida da Hipotenusa: {Medida_da_Hipotenusa:.2f}')

