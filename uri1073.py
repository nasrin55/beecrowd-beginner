n = int(input())
m = 2
m = int(m)
for i in range(1,n+1):
    if n>5 and n<2000 and i%2 == 0:
        r = pow(i,2)
        r = int(r)
        print(f'{i}^{m} = %i'% r)