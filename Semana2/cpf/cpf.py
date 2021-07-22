cpf1 = int(input())

ultimos_digitos_cpf1 = cpf1 // 100
isolar_digitos_cpf1 = cpf1 - (ultimos_digitos_cpf1 * 100)

ultimo_digito_cpf1 = isolar_digitos_cpf1 % 10

penultimo_digito_cpf1 = isolar_digitos_cpf1 // 10
soma_digitos_cpf1 = penultimo_digito_cpf1 + ultimo_digito_cpf1

print(f'{ultimos_digitos_cpf1}-{isolar_digitos_cpf1}')
print(soma_digitos_cpf1)

cpf2 = int(input())

ultimos_digitos_cpf2 = cpf2 // 100
isolar_digitos_cpf2 = cpf2 - (ultimos_digitos_cpf2 * 100)

ultimo_digito_cpf2 = isolar_digitos_cpf2 % 10

penultimo_digito_cpf2 = isolar_digitos_cpf2 // 10
soma_digitos_cpf2 = penultimo_digito_cpf2 + ultimo_digito_cpf2

print(f'{ultimos_digitos_cpf2}-{isolar_digitos_cpf2}')
print(soma_digitos_cpf2)

cpf3 = int(input())

ultimos_digitos_cpf3 = cpf3 // 100
isolar_digitos_cpf3 = cpf3 - (ultimos_digitos_cpf3 * 100)

ultimo_digito_cpf3 = isolar_digitos_cpf3 % 10

penultimo_digito_cpf3 = isolar_digitos_cpf3 // 10
soma_digitos_cpf3 = penultimo_digito_cpf3 + ultimo_digito_cpf3

print(f'{ultimos_digitos_cpf3}-{isolar_digitos_cpf3}')
print(soma_digitos_cpf3)


