o = input()
arr = []
for i in range(12):
    arr.append([])
    for j in range(12):
        x = float(input())
        arr[i].append(x)
if(o == 'S'):
    sum = 0
    for i in range(12):
        for j in range(12):
            if(j<i and (i+j)>11):
                sum = sum + arr[i][j]
    print('{:.1f}'.format(sum))

if(o == 'M'):
    sum = 0
    c = 0
    for i in range(12):
        for j in range(12):
            if(j<i and (i+j)>11):
                sum = sum + arr[i][j]
                c = c + 1
    avg = sum / c
    print('{:.1f}'.format(avg))