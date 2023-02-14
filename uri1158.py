test_case = int(input())
sum = 0
for i in range(1, test_case+1):
    x,y = list(map(int, input().split()))
    if(x%2 == 1):
        sum = 0
        for j in range(1, y+1):
            sum = sum + x
            x = x + 2
        print(sum)
    else:
        x = x + 1
        sum = 0
        for j in range(1, y+1):
            sum = sum + x
            x = x + 2
        print(sum)
