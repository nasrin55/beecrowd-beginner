j = 0
while(j != 1):
    x,y = input().split()
    x = int(x)
    y = int(y)
    if(x<y):
        print('Crescente')
    elif(x>y):
        print('Decrescente')

    if(x == y):
        j = 1