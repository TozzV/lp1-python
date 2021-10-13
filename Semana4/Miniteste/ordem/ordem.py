palavras = input()

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for letra in palavras:
    letra = palavras.split(', ')
    if letra > alfabeto:
        print('em ordem')
    else:
        print('fora de ordem')
