while True:
    n = int(input())
    if n == 0:
        break
    m = []
    for i in range(0, n):
        m.append([])
        for j in range(0, n):
            m[i].append(0)
    for i in range(n):
        a = i+1
        k = 2
        for j in range(0,i+1):
           m[i][j] = a
           a -= 1
        for j in range(i+1,n):
            m[i][j] = k
            k += 1

    for i in range(0, n):
        tx = ''
        for j in range(0, n):
            tx = tx + ' %3d' %m[i][j]
        print(tx[1:])
    print("")
