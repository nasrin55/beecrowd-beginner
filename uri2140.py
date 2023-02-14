lst = [7,12,22,52,102,15,25,55,105,30,60,110,70,120,150]
while True:
    n,m = map(int, input().split())
    if n==0 and m==0:
        break
    r = m - n
    t = 0
    for i in range(len(lst)):
        if(lst[i] == r):
            t = 1
            break
    if(t):
        print('possible')
    else:
        print('impossible')