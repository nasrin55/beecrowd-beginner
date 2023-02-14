x,y = map(int, input().split())
if(x == 1):
    total = 4.00 * y
    print('Total: R$ %.2lf'%total)
if(x == 2):
    total = 4.50 * y
    print('Total: R$ %.2lf' % total)
if(x == 3):
    total = 5.00 * y
    print('Total: R$ %.2lf' % total)
if(x == 4):
    total = 2.00 * y
    print('Total: R$ %.2lf' % total)
if(x == 5):
    total = 1.50 * y
    print('Total: R$ %.2lf' % total)