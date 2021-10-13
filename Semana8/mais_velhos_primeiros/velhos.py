def idosos_inicio(fila):
    contador = 0
    for i in range(len(fila)):
        if fila[i] >= 60:
            fila[i], fila[contador] = fila[contador], fila[i]
            contador += 1

fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
idosos_inicio(fila)
assert fila == [67, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34]
