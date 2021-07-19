adulto = float(input())
crianca = float(input())
ingresso_preco = float(input())

entrada_adultos = adulto * ingresso_preco
entrada_crianca = crianca * ( ingresso_preco / 2 )

total = entrada_adultos + entrada_crianca

print(f'Total: R$ {total:.2f}')

