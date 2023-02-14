n = int(input())
for n in range(0, n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if (y == 0):
        print('divisao impossivel')
    else:
        z = x / y
        print('{:.1f}'.format(z))