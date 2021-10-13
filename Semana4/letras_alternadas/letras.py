palavra = input()

for i in list(range(len(palavra) // 2 + 1)):
    if i == 0:
        print(palavra[0],end="")
    else:
        print(palavra[i * 2],end="")

print("")
