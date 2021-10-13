quantidade_alunos = int(input())
acertos = 0
acertou = '.'
erros = 0

for i in range(quantidade_alunos):
    performace_aluno = input()
    nota = 0
    for j in performace_aluno:
        if j != acertou:
            nota += 1

        if nota > erros:
            erros = nota
            acertos = i + 1

print(f'O aluno {acertos} errou {erros} teste(s).')