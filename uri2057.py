s,t,f = map(int, input().split())
if s == 0:
    s = 24
ans = s+t+f
if ans>24:
    ans -= 24
    print(ans)
elif ans==24:
    ans = 0
    print(ans)
else:
    print(ans)