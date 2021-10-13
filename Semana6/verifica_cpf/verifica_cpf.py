def calcula_digitos_verificacao(cpf):
    cpf = list(cpf)
    soma = 0
    multiplicador = 2
    for i in range(len(cpf)-1, -1, -1):
         soma += int(cpf[i]) * multiplicador
         multiplicador +=1
         if i == 0:
             soma = soma * 10 % 11
             cpf.append(str(soma))
             multiplicador = 2
             soma = 0
    for i in range(len(cpf)-1, -1, -1):
         soma += int(cpf[i]) * multiplicador
         if i == 0:
             soma = soma * 10 % 11
             cpf.append(str(soma))
    return cpf[-2]+cpf[-1]

assert calcula_digitos_verificacao('153245875') == '40'
assert calcula_digitos_verificacao('700881204') == '30'




        


