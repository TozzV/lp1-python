producao = input().split(",")
seq = [1,3,6,8,0,1]

for i in range(len(producao)):
    inteiro = int(i)
    soma_bimestre = producao[inteiro] + producao[inteiro + 1]
    print(soma_bimestre)
