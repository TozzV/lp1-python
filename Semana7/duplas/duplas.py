def remove_duplas(lista):
    while True:
        for i in range(len(lista)):
            contador = 0
            o1 = ''
            o2 = ''
            for j in range(len(lista)):
                if lista[i] == lista[j]:
                    contador +=1
                    if o1 == '' and o2 == '':
                        o1 = i
                    else:
                        o2 = j -1
            if contador == 2:
                lista.pop(o1)
                lista.pop(o2)
                break                    
        if i == (len(lista)-1):
            break