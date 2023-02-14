n,q = map(int, input().split())
arr = [int(x) for x in input().split()]
result = 0
for i in range(q):
    l,r = map(int, input().split())
    result = sum(arr[l-1:r])
    print(result)
