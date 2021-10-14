msg = "Exemplo 2!"

alfabetoMinusculo = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']

def cesar(msg, d):
    palavraNova = ''
    caractereNãoTrocavel = ''
    for i in range(len(msg)):
        for j in range(len(alfabetoMinusculo)):
            if msg[i] == alfabetoMinusculo[j]:
                x = j+int(d)
                if x > 25:
                    x = -1 + (x - 25)
                troca = alfabetoMinusculo[x]
                palavraNova += troca
        if msg[i] not in alfabetoMinusculo:
            palavraNova += msg[i]
    return palavraNova


assert cesar("exemplo", 4) == "ibiqtps"
assert cesar("Exemplo 2!", 4) == "Ebiqtps 2!"
assert cesar("2! Exemplo", 4) == "2! Ebiqtps"
assert cesar("v1t0r", 2) == "x1v0t"