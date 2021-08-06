idade = int(input())

valor_ingresso_crianca = 10.00
valor_ingresso_adulto = 20.00
valor_ingresso_idoso = 12.00

if idade <= 12:
    nome = input('Nome: ')
    documento = ''
    valor_ingresso = valor_ingresso_crianca
    

if idade >= 13 and idade <= 18:
    nome = input('Nome: ')
    documento = int(input('Documento: '))
    valor_ingresso = valor_ingresso_crianca
    

if idade >= 60:
    nome = input('Nome: ')
    documento = int(input('Documento: '))
    valor_ingresso = valor_ingresso_idoso
    

if idade >= 19 and idade <= 59:
    nome = "anônimo"
    documento = ''
    valor_ingresso = valor_ingresso_adulto

print('===')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Documento: {documento}')
print(f'Preço: {valor_ingresso:.2f}')