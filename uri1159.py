sum = 0
while(1):
    n = int(input())
    if(n == 0):
        break
    if(n%2 == 0):
        sum = 0
        for i in range(1,6):
            sum = sum + n
            n = n + 2
        print(sum)
    else:
        n = n + 1
        sum = 0
        for i in range(1,6):
            sum = sum + n
            n = n + 2
        print(sum)
