palavra1 = input()
palavra2 = input()

for i in list(range(len(palavra2))):
    contador = 0 
    for j in list(range(len(palavra1))):
        if palavra1[j] == palavra2[i]:
            if contador > 0:
                print(" ", end = "")
            print(j, end = "")
            contador += 1
    x = (len(palavra2)-1)
    if contador == 0:
        print(-1)
    else:
        print("")