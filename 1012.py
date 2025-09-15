# a,b,c= map(float,input().split())
# a, b, c = float(input().split())
a, b, c = map(float, input().split())
#muito horrivel essa parte de cima slk... beecrowd n ajuda. 
areatriangulo = (a * c) / 2
pi =  3.14159
areacirculo = pi * c**2
areatrapezio = (a + b) * c / 2 
areaquadrado = b**2
arearetangulo =  a * b
print(f'TRIANGULO: {areatriangulo:.3f}') 
print(f'CIRCULO: {areacirculo:.3f}')
print(f'TRAPEZIO: {areatrapezio:.3f}')
print(f'QUADRADO: {areaquadrado:.3f}')
print(f'RETANGULO: {arearetangulo:.3f}')