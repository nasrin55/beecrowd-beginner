s = 0
p = 0
j = 0
while(j != 1):
    n = float(input())
    if(n<0 or n>10):
        print('nota invalida')
    else:
        s = s + n
        p = p + 1
        if(p == 2):
            print('media = %.2f' %(s/2))
            print('novo calculo (1-sim 2-nao)')
            j = 0
            while(j != 1):
                n = float(input())
                if(int(n) == 1):
                    s = p = 0
                    k = 1
                    break
                elif(int(n) == 2):
                    j = 1
                else:
                    print('novo calculo (1-sim 2-nao)')