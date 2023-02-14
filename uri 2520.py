while True:
    try:
        n, m = map(int, input().split())
        matrix = []

        for i in range(n):
            matrix.append(input().split())

        a = [(i, j.index('2')) for i,j in enumerate(matrix) if '2' in j]
        b = [(i, j.index('1')) for i,j in enumerate(matrix) if '1' in j]

        x = (abs(a[0][0] - b[0][0]))
        y = (abs(a[0][1] - b[0][1]))
        print(x + y)


    except EOFError:
        break

