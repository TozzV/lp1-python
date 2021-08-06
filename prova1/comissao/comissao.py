# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Comissao vendedor
# Objetivo do código: calcular a comissao de um vendedor a partir do valor de suas vendas. 

nome_vendedor = input()
venda_realizada = float(input())

base_comissao = venda_realizada / 100

if venda_realizada <= 499.99:
    calcula_comissao = base_comissao * 2
    print(f'O valor da comissão para o(a) vendedor(a) {nome_vendedor} é R$ {calcula_comissao:.2f}.')
elif venda_realizada >= 500.00 and venda_realizada <= 999.99:
    calcula_comissao = base_comissao * 3
    print(f'O valor da comissão para o(a) vendedor(a) {nome_vendedor} é R$ {calcula_comissao:.2f}.')
else:
    calcula_comissao = base_comissao * 4
    print(f'O valor da comissão para o(a) vendedor(a) {nome_vendedor} é R$ {calcula_comissao:.2f}.')