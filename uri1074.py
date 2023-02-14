lis = []
n = int(input())
for i in range(1,n+1):
    lis.append(int(input()))

for n1 in lis:
    if (n1 == 0):
        print('NULL')
    elif (n1 < 0 ):
        if(n1%2 == 0):
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')

    elif (n1 > 0 ):
        if(n1 % 2 == 0):
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')

