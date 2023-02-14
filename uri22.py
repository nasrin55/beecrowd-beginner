import math
n = float(input())
a = int(n/100)
print('NOTAS:')
print("%i nota(s) de R$ 100.00" % a)
b = n % 100
c = int(b/50)
print("%i nota(s) de R$ 50.00" % c)
d = b % 50
e = int(d/20)
print("%i nota(s) de R$ 20.00" % e)
f = d % 20
g = int(f/10)
print("%g nota(s) de R$ 10.00" % g)
h = f % 10
i = int(h/5)
print("%i nota(s) de R$ 5.00" % i)
j = h % 5
k = int(j/2)
print("%i nota(s) de R$ 2.00" % k)
l = j % 2
print('MOEDAS:')
print("%i moeda(s) de R$ 1.00" % l)
E = n*100
B = int(E)
m = B % 100
o = int(m/50)
print("%i moeda(s) de R$ 0.50" % o)
p = m % 50
q = int(p/25)
print("%i moeda(s) de R$ 0.25" % q)
r = p % 25
s = int(r/10)
print("%i moeda(s) de R$ 0.10" % s)
t = r % 10
u = int(t/5)
print("%i moeda(s) de R$ 0.05" % u)
v = t % 5
print("%i moeda(s) de R$ 0.01" % v)
print('\n')