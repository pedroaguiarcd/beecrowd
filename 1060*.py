# lista = []
# cont = 0
# while True:
#     if cont < 6:
#         nums1 = input()
#         cont += 1
#         lista.append(nums1)
#     else:
#         break


lista_nums = []
count = 0

for i in range(6):
    nums = float(input())
    lista_nums.append(nums)  # adiciona nums na lista
    if nums > 0:
        count += 1

print(f"{count} valores positivos")
