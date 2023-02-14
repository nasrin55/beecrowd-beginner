n = int(input())
m = 0.0
al = 0
for i in range(n):
    a,b = input().split()
    if float(b) > m:
        m = float(b)
        al = int(a)

if m >= 8:
    print(al)
else:
    print('Minimum note not reached')