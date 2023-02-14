def result(n):
    if n==0:
        return 2
    x = 2 + 1/result(n-1)
    return x

n = int(input())
x = result(n) - 1
print('%.10f' %x)