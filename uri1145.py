x,y = input().split()
x = int(x)
y = int(y)
n = 0
if(1<x<20 and x<y<100000):
    for i in range(1, y + 1):
        print(i, end=' ')
        n = n + 1
        if (n == x):
            print("")
            n = 0