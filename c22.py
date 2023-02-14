n,m = input().split()
n = int(n)
m = int(m)
arr = []
for i in range(n):
    single_row = list(map(int, input().split()))
    arr.append(single_row)

#print(arr[::-1])

def reverse_arr(arr):
    for i in range(n):
        start = 0
        end = m - 1
        while(start < end):
            arr[i][start], arr[i][end] = arr[i][end], arr[i][start]

            start += 1
            end -= 1
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=' ')
        print()

reverse_arr(arr)
