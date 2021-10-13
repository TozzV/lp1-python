limite = int(input())
pen = 0
ult = 1
print(pen)
if limite >= 2:
    ult = 1
    while True:
        print(ult)
        ult = pen + ult
        pen = ult - pen
        if ult >= limite:
            break
else:
    print("O número tem que ser maior ou igual a 2")
    
