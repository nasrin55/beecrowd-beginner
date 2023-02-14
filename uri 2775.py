while True:
    try:

        n = int(input())
        p = [int(x) for x in input().split()]
        t = [int(x) for x in input().split()]

        sum = 0
        for _ in range(0, n - 1, 1):
            a = 0
            for i in range(0, n - 1, 1):
                if p[i] > p[i + 1]:
                    sum += (t[i] + t[i + 1])
                    aux = p[i]
                    p[i] = p[i + 1]
                    p[i + 1] = aux

                    aux = t[i]
                    t[i] = t[i + 1]
                    t[i + 1] = aux
                    a = 1

            if a == 0:
                break

        print(sum)
    except EOFError:
        break