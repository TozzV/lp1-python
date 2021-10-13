numero1 = int(input())
numero2 = int(input())

if numero2 > numero1:
    numero1, numero2 = numero2, numero1

while(True):
    print(f'maior: {numero1}')
    print(f'menor: {numero2}')
        
    if numero2 <= 0:
        print('----------')
        print(f'MDC: {numero1}')
        break

    resto = numero1 % numero2

    print(f'resto: {resto}')
    print('----------')

    numero1 = numero2
    numero2 = resto


    

        


