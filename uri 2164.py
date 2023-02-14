import math

n = float(input())

v = math.sqrt(5)
r1 = pow(((1+v)/2), n)
r2 = pow(((1-v)/2), n)
result = (r1- r2)/v

print('%.1f' %result)
