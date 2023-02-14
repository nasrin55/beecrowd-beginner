while True:
    try:
        n = []
        c = []
        m = int(input())
        for i in range(m):
            x, y = list(input().split())
            n.append(x)
            c.append(y)

        a = 0
        b = 0
        for i in range(m):
            a += int(n[i]) * int(c[i])
            b = (b + int(c[i]))

        print('%.4f' % (a / (b * 100)))

    except EOFError:
        break