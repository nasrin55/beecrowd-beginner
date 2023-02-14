import math
a,b,s = input().split()
a = int(a)
b = int(b)
s = int(s)

MaiorAB = ((a+b+abs(a-b))/2)
max = ((MaiorAB + s + abs(MaiorAB - s)) / 2)
print('%i eh o maior' %max)
