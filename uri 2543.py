while True:
    try:
        n, id = input().split()
        count = 0
        n = int(n)
        for x in range(n):
            i, j = input().split()
            if i == id and j == '0':
                count += 1
        print(count)
    except EOFError:
        break
