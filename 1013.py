a,b,c = map(int,input().split()) 
maiorab = (a + b + abs(a - b)) // 2
maior_abc = (maiorab + c + abs(maiorab - c)) // 2
print(f"{maior_abc} eh o maior")