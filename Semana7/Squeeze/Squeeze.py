def squeeze(valores):
    while True:
        if len(valores) == 1:
            break
        for i in range(len(valores)-1):
            if valores[i] == valores[i+1]:
                valores.pop(i)
                break
        if i == (len(valores)-2):
            break
    return valores
