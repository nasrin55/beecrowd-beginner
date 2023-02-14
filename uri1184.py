o = input()
arr = []
for i in range(12):
    arr.append([])
    for j in range(12):
        x = float(input())
        arr[i].append(x)

if(o == 'S'):
    sum = 0
    c = 1
    for i in range(12):
        for j in range(12):
            if(i>j):
                sum = sum + arr[i][j]
        #c = c + 1
    print('{:.1f}'.format(sum))
if(o == 'M'):
    s = 0
    c1 = 0
    c2 = 0
    for i in range(12):
        for j in range(12):
            if(i>j):
               s = s + arr[i][j]
            #c2 = c2 + 1
        #c = c + 1
    avg = s/(66)
    print('{:.1f}'.format(avg))