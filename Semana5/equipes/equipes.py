lista = []
while True:
    nome = input()
    if nome == "-":
        break
    else:
        lista += [nome]
if len(lista) == 11:
    print("Modalidade -> Futebol")
elif len(lista) == 7:
    print("Modalidade -> Handebol")
elif len(lista) == 6:
    print("Modalidade -> Vôlei")
elif len(lista) == 5:
    print("Modalidade -> Basquete")
else:
    print("Equipe Inválida")