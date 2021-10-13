def maioridade_penal(nome,idade):
    nome = nome.split(" ")
    idade = idade.split(" ")
    pessoa = ''
    for i in range(0, len(nome)):
        if int(idade[i]) >= 18 and pessoa == '':
            pessoa += nome[i]
        elif int(idade[i]) >= 18:
            pessoa += ' ' + nome[i]
    return pessoa

assert maioridade_penal("Jansen Italo Ana","14 21 60") == "Italo Ana"
assert maioridade_penal("Gustavo Kaio Jacinto","14 15 16") == ""
assert maioridade_penal("Vitor James Kameron","18 19 20") == "Vitor James Kameron"