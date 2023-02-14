def result(n):
    if n==0:
        return 6
    x = 6 + 1/result(n-1)
    return x

n = int(input())
x = result(n) - 3
print('%.10f' %x)