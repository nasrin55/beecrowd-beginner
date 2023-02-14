s = float(input())

if s>0 and s <= 2000.00:
    print('Isento')
elif s>2000 and s<=3000.00:
    r = s - 2000
    t = r * 0.08
    print('R$ %.2lf' % t)
elif s>3000 and s<=4500.00:
    r = s - 3000
    t = (r * 0.18) + (1000 * 0.08)
    print('R$ %.2lf' % t)
else:
    r = s - 4500
    t = (r * 0.28) + (1500 * 0.18) + (1000 * 0.08)
    print('R$ %.2lf' % t)