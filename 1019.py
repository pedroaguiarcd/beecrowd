valor_d_tempo = int(input())
horas = valor_d_tempo // 3600
minutos = (valor_d_tempo % 3600)// 60
segundos = valor_d_tempo % 60
print(f"{horas}:{minutos}:{segundos}")