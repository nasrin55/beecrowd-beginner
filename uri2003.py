while True:
    try:
        h = input().split(":")
        delay = int(h[0])*60 + int(h[1]) - 420
        if delay < 0:
            delay = 0
        print('Atraso maximo: %d' % delay)

    except EOFError:
        break