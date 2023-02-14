x,y = map(int, input().split())


for i in range(y):
    z = input()
    if z == 'fechou':
        x += 1
    else:
        x -= 1
print(x)