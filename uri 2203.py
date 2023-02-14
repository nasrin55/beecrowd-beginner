import math

while True:
    try:
        xf, yf, xi, yi, vi, r1, r2 = [int(x) for x in input().split()]
        d = math.sqrt(math.pow((xf - xi),2) + math.pow((yf - yi), 2))
        if (r1+r2) >= d + 1.5 * vi:
            print('Y')
        else:
            print('N')
    except EOFError:
        break
