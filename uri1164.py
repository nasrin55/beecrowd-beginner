t = int(input())
for i in range(t):
    n = int(input())
    sum = 0
    for j in range(1, n):
        if (n % j == 0):
            sum = sum + j
    if (n == sum):
        print('%d eh perfeito' %n)
    else:
        print('%d nao eh perfeito' %n)