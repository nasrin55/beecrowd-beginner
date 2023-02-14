while True:
    try:
        n, amin, amax = map(int, input().split())
        count = 0
        for i in range(n):
            height = int(input())
            if height >= amin and height <= amax:
                count += 1
        print(count)

    except EOFError:
        break