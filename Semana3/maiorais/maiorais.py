gols_campinense = int(input())
gols_treze = int(input())

campinense_venceu = gols_campinense > gols_treze
treze_venceu = gols_treze > gols_campinense
empate = gols_campinense == gols_treze

if campinense_venceu:
    print('Campinense')
elif treze_venceu:
    print('Treze')
else:
    print('Empate')
