competidor1_nome = input()
competidor1_tentativa1 = int(input())
competidor1_tentativa2 = int(input())
competidor1_tentativa3 = int(input())

competidor2_nome = input()
competidor2_tentativa1 = int(input())
competidor2_tentativa2 = int(input())
competidor2_tentativa3 = int(input())

if competidor1_tentativa1 < competidor1_tentativa2:
    competidor1_menor = competidor1_tentativa1
elif competidor1_tentativa1 < competidor1_tentativa3:
    competidor1_menor = competidor1_tentativa1
elif competidor1_tentativa2 < competidor1_tentativa1:
    competidor1_menor = competidor1_tentativa2
elif competidor1_tentativa2 < competidor1_tentativa3:
    competidor1_menor = competidor1_tentativa2
elif competidor1_tentativa3 < competidor1_tentativa1:
    competidor1_menor = competidor1_tentativa3
elif competidor1_tentativa3 < competidor1_tentativa2:
    competidor1_menor = competidor1_tentativa3

print(competidor1_menor)

if competidor1_tentativa1 > competidor1_tentativa2:
    competidor1_maior = competidor1_tentativa1
elif competidor1_tentativa1 > competidor1_tentativa3:
    competidor1_maior = competidor1_tentativa1
elif competidor1_tentativa2 > competidor1_tentativa1:
    competidor1_maior = competidor1_tentativa2
elif competidor1_tentativa2 > competidor1_tentativa3:
    competidor1_maior = competidor1_tentativa2
elif competidor1_tentativa3 > competidor1_tentativa1:
    competidor1_maior = competidor1_tentativa3
elif competidor1_tentativa3 > competidor1_tentativa2:
    competidor1_maior = competidor1_tentativa3

print(competidor1_maior)

media_competidor1 = (competidor1_maior + competidor1_menor) / 2 
print(media_competidor1)

if competidor2_tentativa1 < competidor2_tentativa2:
    competidor2_menor = competidor2_tentativa1
elif competidor2_tentativa1 < competidor2_tentativa3:
    competidor2_menor = competidor2_tentativa1
elif competidor2_tentativa2 < competidor2_tentativa1:
    competidor2_menor = competidor2_tentativa2
elif competidor2_tentativa2 < competidor2_tentativa3:
    competidor2_menor = competidor2_tentativa2
elif competidor2_tentativa3 < competidor2_tentativa1:
    competidor2_menor = competidor2_tentativa3
elif competidor2_tentativa3 < competidor2_tentativa2:
    competidor2_menor = competidor2_tentativa3

print(competidor2_menor)

if competidor2_tentativa1 > competidor2_tentativa2:
    competidor2_maior = competidor2_tentativa1
elif competidor2_tentativa1 > competidor2_tentativa3:
    competidor2_maior = competidor2_tentativa1
elif competidor2_tentativa2 > competidor2_tentativa1:
    competidor2_maior = competidor1_tentativa2
elif competidor2_tentativa2 > competidor2_tentativa3:
    competidor2_maior = competidor2_tentativa2
elif competidor2_tentativa3 > competidor2_tentativa1:
    competidor2_maior = competidor1_tentativa3
elif competidor2_tentativa3 > competidor2_tentativa2:
    competidor2_maior = competidor2_tentativa3

print(competidor2_maior)

media_competidor2 = (competidor2_maior + competidor2_menor) / 2 
print(media_competidor2)

if media_competidor1 > media_competidor2:
    print("primeiro ganhou")