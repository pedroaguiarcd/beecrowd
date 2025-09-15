# print("#"*7 + " Nosso Cardapio " + "#"*7)
# print("Digite '1' para CACHORRO QUENTE\nDigite '2' para X-SALADA\nDigite '3' para X-BACON\n" \
# "Digite '4' para TORRADA SIMPLES\nDigite '5' para REFRIGERANTE\nApos digitar o codigo do " \
# "produto, digite tambem em sequencia, com espaço entre os numeros a quantidade: " )

# try:
# lanches = {
#     "abc" : ['hotdog', 4.00],
#     2 : ['x-salada', 4.50],
#     3 : ['x-bacon', 5.00],
#     4 : ['Torrada', 2.00],
#     5 : ['refrigerante', 1.50]
# }
lanches = {
    "abc": 5.00,
    2: 4.00,
    3: 3.00,
    4: 3.00,
    5: 2.00
}
cod, qtd = input().split()
qtd = int(qtd)
cod = int(cod)
print(f"Total: R$ {(lanches[cod]) * qtd}")
