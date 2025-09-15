lanches = {
    1: ("hotdog", 4.00),
    2: ("x-salada", 4.50),
    3: ("x-bacon", 5.00),
    4: ("torrada", 2.00),
    5: ("refrigerante", 1.50)
}

code, amount = map(int, input().split())
valortotal = lanches[code][1] * amount
# esse lanche[code] vai no dicionario pegar o item que
print(f"Total: R$ {float(valortotal):.2f}")
# o usuario colocou em code.
# Então, no nosso exemplo, como cod é 2, o código
# vai olhar no dicionário lanches qual é o valor
# associado à chave 2. E como você viu, o valor de lanches[2] é 4.50.
