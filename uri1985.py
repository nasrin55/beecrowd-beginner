t = int(input())
sum = 0
for i in range(t):
    a,b = input().split()
    b = int(b)
    if a=='1001':
        sum = sum + (b*1.50)
    elif a=='1002':
        sum = sum + (b*2.50)
    elif a=='1003':
        sum = sum + (b*3.50)
    elif a=='1004':
        sum = sum + (b*4.50)
    elif a=='1005':
        sum = sum + (b*5.50)
print('%.2f'%sum)