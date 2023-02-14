fibo = [0,1,1]
r = '0,1,1'
n1 = 1
n2 = 1
n = int(input())
for i in range(n - 3):
    t = n2
    n2 = n2 + n1
    n1 = t
    fibo.append(n2)

print(str(fibo[0:n]).replace(",", "").replace("[", "").replace("]", ""))
