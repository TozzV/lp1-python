def bubblesort(dados):
    while(True):
        swapped = False
        for i in range(0, len(dados) - 1):
            if dados[i] > dados[i+1]:
                dados[i],dados[i+1] = dados[i+1], dados[i]
                swapped = True
        if swapped == False:
            break
        