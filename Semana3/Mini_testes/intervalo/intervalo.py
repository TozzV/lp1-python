menor_intervalo = int(input())
maior_intervalo = int(input())
valor_avaliacao = int(input())

antes = valor_avaliacao < menor_intervalo
dentro = (valor_avaliacao >= menor_intervalo) and (valor_avaliacao <= maior_intervalo)
depois = valor_avaliacao > maior_intervalo

if antes:
    print('antes')
elif dentro:
    print('dentro')
else:
    print('depois')