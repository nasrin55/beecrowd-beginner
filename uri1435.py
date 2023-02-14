while True:
    n = int(input())
    if n == 0:
        break
    m = []
    for i in range(0, n):
        m.append([])
        for j in range(0, n):
            m[i].append(0)
    if n % 2 == 0:
        t = n // 2
    else:
        t = 1 + n // 2

    min = 0
    max = n
    cont = 0
    for k in range(0, t):
        cont += 1
        for i in range(min, max):
            for j in range(min, max):
                m[i][j] = cont
        min += 1
        max -= 1

    for i in range(0, n):
        tx = ''
        for j in range(0, n):
            tx = tx + ' %3d' %m[i][j]
        print(tx[1:])
    print("")
