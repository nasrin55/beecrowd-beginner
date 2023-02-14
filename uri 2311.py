n = int(input())

for i in range(n):
    name = input()
    d = float(input())
    x = [float(i) for i in input().split()]
    r = sum(sorted(x)[1:6]) * d
    print('%s %.2f' %(name, r))