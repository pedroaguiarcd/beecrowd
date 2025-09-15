num = int(input())
cont = 0
while cont < 6:
    impar = num % 2
    cont += 1
    if impar == 0:
        num += 1
    else:
        num += 2
    print(num)
