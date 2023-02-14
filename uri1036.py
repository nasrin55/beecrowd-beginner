import math
a,b,c = list(map(float, input().split()))
d = b*b - 4*a*c
e = pow(d, .5)
if(d<0 or a==0):
    print('Impossivel calcular')
else:
    r1 = (-b + e) / (2*a)
    print('R1 = %.5lf'%r1)
    r2 = (-b - e) / (2*a)
    print('R2 = %.5lf'%r2)