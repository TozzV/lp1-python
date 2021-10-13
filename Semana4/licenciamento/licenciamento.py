placa = input().split(" ")

mes = ['janeiro', 'fevereiro','março','abril','maio'
,'junho','julho','agosto','setembro','outubro']

for j in range(len(placa)):
    consulta = placa[j][-1]
    relacao = mes[int(consulta) - 1]
    print(f'{placa[j]}: {relacao}')

