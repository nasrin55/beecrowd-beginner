while(1):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if(x==0 or y==0):
        break
    if (x > 0 and y > 0):
        print('primeiro')
    elif (x > 0 and y < 0):
        print('quarto')
    elif (x < 0 and y > 0):
        print('segundo')
    elif (x < 0 and y < 0):
        print('terceiro')