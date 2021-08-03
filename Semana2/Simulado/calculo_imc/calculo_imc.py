# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Cálculo IMC
# Objetivo do código: Calcular o IMC de um paciente

peso = float(input())
altura = float(input())

imc = peso / ( altura **2 )
print(f'IMC = {imc:.1f}')

if imc < 18.5:
    print("Classificação = Magreza")

if 18.5 <= imc < 25:
    print("Classificação = Saudável")

if 25 <= imc < 30:
    print("Classificação = Sobrepeso")

if imc >= 30:
    print("Classificação = Obesidade")