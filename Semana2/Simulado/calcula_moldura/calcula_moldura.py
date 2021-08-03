comprimento = float(input())
largura = float(input())

preco_metro = 120
area_comprimento = comprimento * 2
area_largura = largura * 2

area_moldura = area_comprimento + area_largura
conversao_metro = area_moldura / 100
preco_moldura = conversao_metro * preco_metro

print(f'R$ {preco_moldura}')