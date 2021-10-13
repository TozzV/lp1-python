def analisa_equidistantes(inteiros):
    p1 = 0
    p2 = (len(inteiros)-1)
    lista = []
    while True:
        if p1 >= ((len(inteiros)-1) // 2) and len(inteiros) % 2 != 0:
            break
        elif p1 > ((len(inteiros)-1) // 2):
            break
        elif (inteiros[p1] % 3 == 0 and inteiros[p2] % 3 == 0) and inteiros[p1] % 5 == 0 and inteiros[p2] % 5 == 0:
            lista += [15]
        elif inteiros[p1] % 3 == 0 and inteiros[p2] % 3 == 0:
            lista += [3]
        elif inteiros[p1] % 5 == 0 and inteiros[p2] % 5 == 0:
            lista += [5]
        else:
            lista += [inteiros[p1]*inteiros[p2]]
        p1 += 1
        p2 -= 1
    if len(inteiros) % 2 != 0:
        lista += [inteiros[p1]]
    return lista