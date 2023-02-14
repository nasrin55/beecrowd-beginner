c = 0
d = 0
while(d < 2):
    a = float(input())
    if(a>=0 and a<=10):
        c = c + a
        d = d + 1
    else:
        print('nota invalida')
print('media = %.2f' %(c/2))