salario_bruto = float(input())
horas_de_trabalho = int(input())

hora_bruta = salario_bruto / horas_de_trabalho

desconto_IR = (11 / 100) * salario_bruto
desconto_INSS =  (8 / 100) * salario_bruto
desconto_sindicato = (5 / 100) * salario_bruto
desconto_total = desconto_IR + desconto_INSS + desconto_sindicato

salario_liquido = salario_bruto - desconto_total 
hora_liquida = salario_liquido / horas_de_trabalho


print(f'Salário Bruto = {salario_bruto:.2f}')
print(f'Hora Bruta = {hora_bruta:.2f}')
print(f'Desconto IR = {desconto_IR:.2f}')
print(f'Desconto INSS = {desconto_INSS:.2f}')
print(f'Desconto Sindicato = {desconto_sindicato:.2f}')
print(f'Salário Líquido = {salario_liquido:.2f}')
print(f'Hora Líquida = {hora_liquida:.2f}')
