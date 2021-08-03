# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Calcula nome
# Objetivo do código: calcular o preço de um produto de 
# acordo com a quantidade de letras do nome do cliente

nome = input("Nome? ")
valor_letra = float(input("Valor da letra (R$)? "))

conta_letras = len(nome)
define_preco = conta_letras * valor_letra

print(f'Preço final: R$ {define_preco:.2f}')