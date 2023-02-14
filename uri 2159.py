from numpy import log

n = int(input())
r1 = n / log(n)
r2 = r1 * 1.25506
print('%.1f ' %r1, '%.1f' %r2)
