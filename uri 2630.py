import math
t = int(input())
for i in range(t):
    s = str(input())
    r,g,b = list(map(int, input().split()))
    if s == 'eye':
        result = int(r*0.3 + g*.59 + b*.11)
        print(f"Caso #{i+1}: {result}")
    elif s == 'min':
        result = min(r,g,b)
        print(f"Caso #{i+1}: {result}")
    elif s == 'max':
        result = max(r,g,b)
        print(f"Caso #{i + 1}: {result}")
    elif s == 'mean':
        result = int((r+g+b)/3)
        print(f"Caso #{i + 1}: {result}")
