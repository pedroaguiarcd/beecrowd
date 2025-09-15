import math
x1,y1 = map(float,input().split())
x2,y2 = map(float,input().split())
p1 = x1,x2
p2 = y1,y2
cal = (x1 - x2)**2 + (y1 - y2)**2
raiz = math.sqrt(cal)
print(f"{raiz:.4f}")