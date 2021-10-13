aluno_quantidade = int(input())

acertos, acertou= 0, "."
erros, errou = 0, "f"
branco, nao_fez= 0, "*"

for i in range(aluno_quantidade):
    validacao = input().split(" ")

    if acertou in list(validacao):
        acertos += len(validacao)
    elif errou in list(validacao):
        erros += len(validacao)
    
