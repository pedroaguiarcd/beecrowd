num = int(input())
seguidos = 0
while seguidos < num:
    if num >= 10 and num <= 20:
        num += 1
        print(f"{num} in")
        # diferenye = num >= 10 and num <= 20

    else:
        print(f'{num} out')
        break
