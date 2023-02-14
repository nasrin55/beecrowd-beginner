while True:
    try:
        t = int(input())
        x = input().split()
        arr = 0
        for i in range(t):
            if (int(x[i]) > arr):
                arr = int(x[i])
        if arr < 10:
            n = 1
        if arr >= 10 and arr < 20:
            n = 2
        if arr >= 20:
            n = 3
        print(n)
    except EOFError:
        break