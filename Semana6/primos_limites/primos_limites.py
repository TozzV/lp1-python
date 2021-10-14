
while True:
    numero = input("numero? ")
    if numero == '':
        break
    numero = int(numero)
    acho_que_eh_primo = True
    i = 2 
    while i < numero and acho_que_eh_primo:
        if numero % i == 0:
            acho_que_eh_primo = False
            break
        i = i + 1
    if acho_que_eh_primo:
        print(f'{numero}: primo')
        return numero 
    else:
        print(f'{numero} não é primo')
        break

    def ListaPrimos(numero):
        



assert primos_ate(10) == [2, 3, 5, 7]
assert primos_ate(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]