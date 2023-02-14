n = int(input())
k = int(input())
candidate = [int(input()) for x in range(n)]
candidate.sort(reverse=True)
ans = k
while ans < n and candidate[ans] == candidate[k-1]:
    ans += 1
#print(candidate[ans], candidate[k-1])
print(ans)