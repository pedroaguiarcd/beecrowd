
# try:
lista_de_numeros = []
contador = 0
for impar in range(5):
    numeros = int(input())
    lista_de_numeros.append(numeros)
    if numeros % 2 == 0:
        contador += 1
print(f"{contador} valores pares")
# except:
#     print("valor nao reconhecido")
