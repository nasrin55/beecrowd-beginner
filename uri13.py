import math
a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)
triangle = (a*c)/2
print('TRIANGULO: %.3f'%triangle)
pi = 3.14159
circle = pi * pow(c,2)
print('CIRCULO: %.3f'%circle)
trap = ((a+b)*c)/2
print('TRAPEZIO: %.3f'%trap)
sqr = pow(b,2)
print('QUADRADO: %.3f'%sqr)
rec = a*b
print('RETANGULO: %.3f' %rec)