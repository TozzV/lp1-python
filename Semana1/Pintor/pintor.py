# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Pintor
# Objetivo do código: Auxiliar um pintor a calcular o valor a ser pago pelo seu serviço.
# O sistema recebe dois valores, sendo o primeiro correspondende a altura e o segundo a largura do 
# local e a partir disso é calculado qual será o valor a ser pago ao pintor. 

altura = float(input())
largura = float(input())

valor_metro_quadrado = 20.00
calculo_metro_quadrado = altura * largura
cliente_valor = calculo_metro_quadrado * valor_metro_quadrado

print(f'R$ {cliente_valor:.2f}')
