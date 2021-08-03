ano_atual = int(input('Ano atual? '))
ano_nascimento = int(input('Ano de nascimento? '))

idade_atual = ano_atual - ano_nascimento
print(f'Idade calculada: {idade_atual} anos')
entra_livremente = idade_atual >= 16
acompanha_pais = (idade_atual <= 16) and (idade_atual >= 14)
nao_entra = idade_atual < 14

if entra_livremente: 
    print(f'Entrada permitida')
elif nao_entra:
    print('Entrada proibida para menores de 14 anos')
elif acompanha_pais:
    pais = input('Com os pais? ')
    if pais == 's':
        print(f'Entrada permitida')
    else:
        print('Entrada proibida para menores de 16 anos sem os pais')


