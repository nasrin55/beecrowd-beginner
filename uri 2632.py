lavel1 = [20, 10, 25, 18]
lavel2 = [30, 25, 55, 38]
lavel3 = [50, 40, 70, 60]

t = int(input())
for i in range(t):
    rec = list(map(int, input().split()))
    identifier = list(input().split())
    if identifier[0] == 'fire' and identifier[1] == '1':
        if sum(lavel1) > sum(rec):
            print(200)
        else:
            print(0)
    elif identifier[0] == 'fire' and identifier[1] == '2':
        if sum(lavel2) > sum(rec):
            print(200)
        else:
            print(0)

    elif identifier[0] == 'fire' and identifier[1] == '3':
        if sum(lavel3) > sum(rec):
            print(200)
        else:
            print(0)

    elif identifier[0] == 'water' and identifier[1] == '1':
        if sum(lavel1) > sum(rec):
            print(300)
        else:
            print(0)

    elif identifier[0] == 'water' and identifier[1] == '2':
        if sum(lavel2) > sum(rec):
            print(300)
        else:
            print(0)

    elif identifier[0] == 'water' and identifier[1] == '3':
        if sum(lavel3) > sum(rec):
            print(300)
        else:
            print(0)

    elif identifier[0] == 'earth' and identifier[1] == '1':
        if sum(lavel1) > sum(rec):
            print(400)
        else:
            print(0)

    elif identifier[0] == 'earth' and identifier[1] == '2':
        if sum(lavel2) > sum(rec):
            print(400)
        else:
            print(0)
    elif identifier[0] == 'earth' and identifier[1] == '3':
        if sum(lavel3) > sum(rec):
            print(400)
        else:
            print(0)

    elif identifier[0] == 'air' and identifier[1] == '1':
        if sum(lavel1) > sum(rec):
            print(100)
        else:
            print(0)

    elif identifier[0] == 'air' and identifier[1] == '2':
        if sum(lavel2) > sum(rec):
            print(100)
        else:
            print(0)

    elif identifier[0] == 'air' and identifier[1] == '3':
        if sum(lavel3) > sum(rec):
            print(100)
        else:
            print(0)
