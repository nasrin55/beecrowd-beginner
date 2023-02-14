p = 1
q = 1
r = 1
n = int(input())
for i in range(1, n+1):
    print('{} {} {}'.format(p,q,r))
    p = p + 1
    q = p * p
    r = q * p