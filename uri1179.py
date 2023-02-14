par = []
impar = []
for i in range(15):
    value = int(input())
    if(value%2 == 0):
        par.append(value)
    else:
        impar.append(value)

    if(len(par) == 5):
        x = 0
        for i in par:
            print('par[%d] = %d' %(x,i))
            x = x + 1
        par = []
    if(len(impar) == 5):
        x = 0
        for i in impar:
            print('impar[%d] = %d' %(x, i))
            x = x + 1
        impar = []
if(len(impar) > 0):
    x = 0
    for i in impar:
        print('impar[%d] = %d' %(x, i))
        x = x + 1


if(len(par) > 0):
    x = 0
    for i in par:
        print('par[%d] = %d' %(x,i))
        x = x + 1