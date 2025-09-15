test_case = int(input())
# bizu para contar:
# enquanto test_case for > 0 pare de contar

# se number = n entao n é 2 - (n-1)
while test_case > 0:
    test_case -= 1
    number = int(input())

    is_prime = True

    for div in range(2, number):
        if number % div == 0:
            is_prime = False
            break
    if is_prime:  # sem o True pq força a variavel a fazer uma logica
        print(number, "eh primo")
    else:
        print(number, "nao eh primo")


# pra saber se é primo: so precisa testar se existe divisor entre n e 10
# so precisaria testar ate a metade do numero pro programa ser mais rapido: exe: 10 e dividir somente ate 5
# porque dps do 5 so vai ser numero quebrado

range(2, number // 2 * number % 2)
