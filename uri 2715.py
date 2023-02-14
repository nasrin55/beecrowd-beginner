while True:
    try:
        n = int(input())
        t = [int(x) for x in input().split()]
        i = 1
        dif = (t[-1]) - sum(t[:-1])
        print(dif)
    except EOFError:
        break