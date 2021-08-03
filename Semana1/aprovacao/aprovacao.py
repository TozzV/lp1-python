# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Aprovação Unidades
# Objetivo do código: Retornar ao usuário sua próxima unidade e a sua média. 

unidade = int(input('Unidade? '))
media = float(input('Média de aprovação na unidade? '))
proxima_unidade = unidade + 1

print(f'\nO aluno vai para a unidade {proxima_unidade} com média {media:.1f}.')