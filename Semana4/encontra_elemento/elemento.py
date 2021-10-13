numero = int(input())
lista = input().split(" ")

contador = 0

for i in lista:
    if i != '':
        i = int(i)
        if i == numero:
            contador += 1    

if contador != 0:
    print("sim")    
else:    
    print("não")   
