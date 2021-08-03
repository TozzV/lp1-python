ruido = input()
horario = int(input())

if ruido == '':
    print('Não houve ruído detectado')
elif horario >= 22:
    print('Pertubação Detectada!')
elif horario <= 6:
    print('Pertubação Detectada!')
else:
    print('Condomínio em Paz.')