area_construida = float(input())
aliquota = float(input())

limpeza_urbana = 35.00

iptu = (area_construida * aliquota) + limpeza_urbana

pagamento_cota =  iptu - ((iptu * 25) / 100)

seis_parcelas = iptu - ((iptu * 5) / 100 ) 
valor_parcela_seis =  seis_parcelas / 6

dez_parcelas = iptu / 10

print(f'Área construída? Alíquota? IPTU: R$ {iptu:.2f}\n')
print('Pagamento:')
print(f'1. Quota única. R$ {pagamento_cota:.2f}')
print(f'2. Em 6 parcelas. Total: R$ {seis_parcelas:.2f}')
print(f'   6 x R$ {valor_parcela_seis:.2f}')
print(f'3. Em 10 parcelas. Total: R$ {iptu:.2f}')
print(f'   10 x R$ {dez_parcelas:.2f}')
