l = int(input())
t = input()
arr = []
for i in range(12):
    arr.append([])
for i in range(12):
    for j in range(12):
        x = float(input())
        arr[i].append(x)
if(t == "S"):
    sum = 0
    for i in range(12):
        sum = sum + arr[i][l]
    print(sum)
if(t == 'M'):
    sum = 0
    for i in range(12):
        sum = sum + arr[i][l]
    avg = sum / 12
    print('{:.1f}'.format(avg))
