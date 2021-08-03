ladoA = int(input())
ladoB = int(input())
ladoC = int(input())

triangulo_valido1 = (ladoB - ladoC) < ladoA < ( ladoB + ladoC )
triangulo_valido2 = (ladoA - ladoC) < ladoB < ( ladoA + ladoC )
triangulo_valido3 = (ladoA - ladoB) < ladoC < ( ladoA + ladoB )

soma_triangulos = ladoA + ladoB + ladoC


if triangulo_valido1:
    print(f'triangulo valido. {soma_triangulos}')
elif triangulo_valido2:
    print(f'triangulo valido. {soma_triangulos}')
elif triangulo_valido3:
    print(f'triangulo valido. {soma_triangulos}')
else: 
    print('triangulo invalido.')