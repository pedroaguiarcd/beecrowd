count_par = 0
count_positivo = 0
count_negativo = 0
for num in range(5):  # vai rodar o loop 5 vezes
    numero = int(input())
    if numero % 2 == 0:
        count_par += 1
    if numero > 0:
        count_positivo += 1
    if numero < 0:
        count_negativo += 1
print(f"{count_par} valor(es) par(es)")
print(f"{5 - count_par} valor(es) impar(es)")
print(f"{count_positivo} valor(es) positivo(s)")
print(f"{count_negativo} valor(es) negativo(s)")
