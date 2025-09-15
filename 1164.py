# test_cases = int(input())
# case = 0

# while case < test_cases:
#     case += 1

#     number = int(input())
#     sum = 0           #soma
#     div = 1           #candidatos a divisao
#     while div < number:
#         if number % div == 0: # se for verdade sum vai receber 1
#             sum += 1
#         div += 1

#     if number == sum:
#         print(number,'eh perfeito')
#     else:
#         print(number,"nao eh perfeito")

# VERSÃO COM FOR (SEM WHILE)

test_cases = int(input())
case = 0

while case <= test_cases:
    case += 1

    number = int(input())
    sum = 0  # soma
    for div in range(1, number):
        if number % div == 0:
            sum += div

    if number == sum:
        print(number, 'eh perfeito')
    else:
        print(number, "nao eh perfeito")


# RANGE:
# tuple(range(10))
# tuple(range(1,10))
