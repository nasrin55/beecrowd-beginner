n = int(input())
c = 0
r = 0
s = 0
for i in range(n):
    a,ch = list(map(str, input().split()))
    a = int(a)
    if ch == 'C':
        c = c + a
    elif ch == 'R':
        r = r + a
    else:
        s = s + a

total = c + r + s
coelho = (c*100)/total
rato = (r*100)/total
sapo = (s*100)/total
print("Total: {} cobaias".format(total))
print("Total de coelhos:",c)
print("Total de ratos:",r)
print("Total de sapos:",s)
print("Percentual de coelhos: %.2lf %%"%coelho)
print("Percentual de ratos: %.2lf %%"%rato)
print("Percentual de sapos: %.2lf %%"%sapo)