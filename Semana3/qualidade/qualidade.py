congelado = float(input())
descongelado = float(input())

delta_peso = congelado - descongelado
porcentagem_agua = ( delta_peso / congelado) * 100

tolerancia_maxima = 10
tolerancia_minima = 5 

em_conformidade = (porcentagem_agua <= tolerancia_maxima) and (porcentagem_agua >= tolerancia_minima)
especial = porcentagem_agua <= tolerancia_minima

if  em_conformidade:
    print(f'{porcentagem_agua:.1f}% do peso do produto é de água congelada.')
    print('Produto em conformidade.')
elif especial:
    print(f'{porcentagem_agua:.1f}% do peso do produto é de água congelada.')
    print('Produto qualis A.')
else:
    print(f'{porcentagem_agua:.1f}% do peso do produto é de água congelada.')
    print('Produto não conforme.')