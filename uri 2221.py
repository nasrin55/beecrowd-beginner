t = int(input())
for i in range(t):
    b = int(input())
    a1, d1, l1 = map(int, input().split())
    a2, d2, l2 = map(int, input().split())

    v1 = (a1 + d1) / 2
    v2 = (a2 + d2) / 2

    if l1 % 2 == 0:
        v1 += b
    if l2 % 2 == 0:
        v2 += b


    if v1 > v2:
        print('Dabriel')
    elif v1 < v2:
        print('Guarte')
    else:
        print('Empate')