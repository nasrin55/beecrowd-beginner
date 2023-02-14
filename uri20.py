import math
n = int(input())
m = int(n/60)
n %= 60
h = int(m/60)
m %= 60
print(f'{h}:{m}:{n}')
