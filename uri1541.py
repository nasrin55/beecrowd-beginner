while True:
    x = input().split()
    if(x == ['0']):
        break
    a,b,c = x
    a,b,c = int(a), int(b), int(c)
    area = a*b*100/c
    area = (area) ** (1/2)
    print(int(area))