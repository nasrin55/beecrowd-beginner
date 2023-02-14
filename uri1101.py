sum = 0
j = 0
while(j != 1):
    m,n = input().split(" ")
    m = int(m)
    n = int(n)
    sum = 0
    if(m>n):
        aux = m
        m = n
        n = aux
    if(m<=0 or n<=0):
        j = 1
    if j != 1:
        for i in range(m,n+1):
            print('%d ' %(i), end="")
            sum = sum + i
            if i == n:
                print("Sum=%d" %(sum))