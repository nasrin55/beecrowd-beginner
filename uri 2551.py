while True:
    try:
        n = int(input())
        t = []
        d = []
        while n:
            n -= 1
            t.append([int(x) for x in input().split()])
            if len(t) == 1:
                m = t[0][1] / t[0][0]
                d.append(1)
            else:
                if t[-1][1] / t[-1][0] > m:
                    m = t[-1][1] / t[-1][0]
                    d.append(1)
                else:
                    d.append(0)
        for i in range(len(d)):
            if d[i] == 1:
                print(i + 1)

    except EOFError:
        break