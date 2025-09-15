sum = 0
count = 0

while True:
    number = int(input())
    if number < 0:
        break
    sum += number
    count += 1
avarage = sum / count
print(f'{avarage:.2f}')
