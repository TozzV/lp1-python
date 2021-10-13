receita_total = []
mes = [
    'jan','fev']

for i in range(3):
    entrada = input().split(" ")
    lucro = float(entrada[0]) - float(entrada[1])
    receita_total.append(lucro)

for j in mes:
    for k in receita_total:
        print(f'{mes[j]}  {k:.1f}')

