sum = 0
x = int(input())
y = int(input())

if(x<y):
    for i in range(x, y + 1):
        if (i % 13 != 0):
            sum = sum + i

if(x>y):
    for i in range(y, x+1):
        if(i % 13 != 0):
            sum = sum + i

print(sum)