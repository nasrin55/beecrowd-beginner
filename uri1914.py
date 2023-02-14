t = int(input())
for i in range(t):
    s1,s2,s3,s4 = input().split()
    n,m = input().split()
    s1 = str(s1)
    s2 = str(s2)
    s3 = str(s3)
    s4 = str(s4)
    n = int(n)
    m = int(m)

    n += m

    if(s2 == "IMPAR"):
        if(n%2 == 0):
            print(s3)
        else:
            print(s1)
    else:
        if(n%2 == 0):
            print(s1)
        else:
            print(s3)