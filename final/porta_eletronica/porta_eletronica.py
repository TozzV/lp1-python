# Universidade Federal de Campina Grande
# Bacharelado em ciências da computação - 2020.2e
# Aluno: José Vitor Barbosa Maciel - Matrícula: 120210954
# Atividade-titulo: Porta eletrônica
# Objetivo do código: registrar e printar pontos de funcionários

registro = []
while True:
    entrada = input()
    if entrada[0] == "R" or entrada[0] == "r" and len(entrada) == 8:
        registro.append(entrada)
    elif entrada[0] == "P" or entrada[0] == "p":
        contador = 0
        for i in range(len(registro)):
            if registro[i][2] == entrada[2]:
                contador +=1
        print(contador)
    elif entrada == "S" or entrada[0] == "s":
        break