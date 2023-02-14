while True:
    try:
        n, m = map(int, input().split())
        mat = [list(map(int, input().split())) for i in range(n)]

        for i in range(n):
            for j in range(m):
                x = 0
                if (i > 0):
                    x += mat[i - 1][j]
                if (i < n - 1):
                    x += mat[i + 1][j]
                if (j > 0):
                    x += mat[i][j - 1]
                if (j < m - 1):
                    x += mat[i][j + 1]
                if (mat[i][j]):
                    print(9, end='')
                else:
                    print(x, end='')
            print()
    except EOFError:
        break