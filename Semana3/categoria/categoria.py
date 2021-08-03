nome_nadador = input()
idade_nadador = int(input())

if (idade_nadador >=5) and (idade_nadador <=7):
    print(f'{nome_nadador}, {idade_nadador} anos, Infantil A.')
elif (idade_nadador >=8) and (idade_nadador <=10):
    print(f'{nome_nadador}, {idade_nadador} anos, Infantil B.')
elif (idade_nadador >= 11) and (idade_nadador <= 13):
    print(f'{nome_nadador}, {idade_nadador} anos, Juvenil A.')
elif (idade_nadador >= 14) and (idade_nadador <= 17):
    print(f'{nome_nadador}, {idade_nadador} anos, Juvenil B.')
elif (idade_nadador >= 17):
    print(f'{nome_nadador}, {idade_nadador} anos, Senior.')   
else:
     print(f'{nome_nadador}, {idade_nadador} anos, Não pode competir.')   
