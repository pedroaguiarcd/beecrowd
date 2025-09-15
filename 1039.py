# import sys 

# for _ in sys.stdin:
while True:
    try:
        R1,X1,Y1,R2,X2,Y2 = map(int,input().split())
        range = (X1 - X2)**2 + (Y1 - Y2)**2 #distancia euclidiana para os centros de cada raio
        range_root = range * 0.5 #raiz da operação acimaa
        # a distancia + raio da flor tem que ser <= que o raio do homem
        result = range + R2 
        if result <= R1:
            print("RICO")
        else:
            print("MORTO")
    except EOFError:
        break
    