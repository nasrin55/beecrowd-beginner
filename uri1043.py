x,y,z = list(map(float, input().split()))
if((x+y)>z and (x+z)>y and (y+z)>x):
    peri = x + y + z
    print('Perimetro = %.1lf' % peri)
else:
    area = ((x+y)*z) / 2
    print('Area = %.1lf' % area)