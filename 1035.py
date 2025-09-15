#codigo corrigido pelo gpt:
a, b, c, d = map(int, input().split())

if (b > c) and (d > a) and ((c + d) > (a + b)) and (c > 0) and (d > 0) and (a % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")



#meu codigo original:
# a,b,c,d = map(int,input().split())
# somacd = c + d
# somaab = a + b
# para = a % 2 #se o resto for == 0 ela é par
# if b > c:
#     if d > a:
#         if somacd > somaab:
#             if c > 0 and d > 0:
#                 if para == 0:
#                     print("Valores aceitos")
# else:
#     print("Valores nao aceitos")