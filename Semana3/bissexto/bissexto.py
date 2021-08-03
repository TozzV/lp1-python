ano = int(input())

bissexto = ( (ano / 400) * 10 ) == (( ano / 4 ) / 10)
nao_bissexto = ( ano / 100 ) != bissexto

if bissexto:
    print(f'{ano} é bissexto')
elif nao_bissexto:
    print(f'{ano} não é bissexto')
else: 
    print(f'{ano} não é bissexto')