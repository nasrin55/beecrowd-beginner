n = int(input())
for i in range(1,11):
    if n>1 and n<1000:
        r = i*n
        print(f'{i} x {n} = %i'% r)