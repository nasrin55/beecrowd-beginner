c = {'suco de laranja':120, 'morango fresco':85, 'mamao':85, 'goiaba vermelha':70, 'manga':56, 'laranja':50, 'brocolis':34}

while(True):
    t = int(input())
    if t == 0:
        break

    vitamin = 0
    for i in range(t):
        w = input().split()
        n = int(w[0])
        frut = ' '.join(w[1:])
        vitamin = vitamin + c[frut] * n
    if vitamin < 110:
        print('Mais %d mg' % (110 - vitamin))
    elif vitamin > 130:
        print('Menos %d mg' % (vitamin - 130))
    else:
        print('%d mg' % vitamin)
