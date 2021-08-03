
morangos_produzidos = int(input())

valor_disponivel_caixa = 400

preencher_caixas = divmod(morangos_produzidos, valor_disponivel_caixa)

caixa_completa = preencher_caixas[0]
morangos_restantes = preencher_caixas[1]

percentual_restante = (morangos_restantes / morangos_produzidos) * 100

print(f'{caixa_completa} caixa(s) completa(s) para embalar os morangos.')
print(f'{percentual_restante:.1f}% dos morangos serão perdidos.')