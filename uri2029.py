while True:
    try:
        v = float(input())
        d = float(input())
        r = d/2
        area = 3.14*r*r
        height = v/area
        print('ALTURA = %.2f' %height)
        print('AREA = %.2f' %area)

    except EOFError:
        break