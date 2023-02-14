while True:
    try:
        n = int(input())
        m = []
        for i in range(0, n):
            m.append([])
            for j in range(0, n):
                m[i].append(0)
        k = n - 1
        for i in range(n):
            for j in range(n):
                if (i == j):
                    m[i][j] = 2
                else:
                    m[i][j] = 0
                if (j == k):
                    m[i][j] = 3
            k -= 1
        l = int(n / 3)
        t = n - l
        for i in range(l, t):
            for j in range(l, t):
                m[i][j] = 1
                if (i == int(n / 2) and j == int(n / 2)):
                    m[i][j] = 4
        for i in range(n):
            tx = ''
            for j in range(n):
                tx += str(m[i][j])
            print(tx)
        print()
    except EOFError:
        break