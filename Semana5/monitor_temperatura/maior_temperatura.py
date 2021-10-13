# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Monitor temperatura
# Objetivo do código: Informar a temperatura inadequada de um aquário, informar a quantidade de temperaturas adequadas medidas e a sua média.

contador = 0
soma = 0

while(True):
    temperaturas = float(input())
    if temperaturas < 10.0 or temperaturas > 30.0:
        media = soma / (contador if contador != 0 else 1)
        print(f'''Temperatura inadequada! {temperaturas:.2f}.
{contador} medições lidas dentro do padrão.
Média = {media:.2f}.''')
        break
    else:
        contador += 1
        soma += temperaturas


