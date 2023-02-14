l = input().split()
y, x = int(l[0]), int(l[1])
m = []

for i in range(y):
    m.append([int(i) for i in input().split()])

t = t2 = 0
for i in range(y):
    for j in range(x):
        m[i][j] = int(m[i][j])

for i in range(1, y-1):
    for j in range(1, x-1):
        if m[i][j] == 42:
            if m[i-1][j-1] == 7 and m[i-1][j] == 7 and m[i-1][j+1] == 7:
                if m[i][j-1] == 7 and m[i][j + 1] == 7:
                    if m[i+1][j-1] == 7 and m[i+1][j] == 7 and m[i+1][j+1] == 7:
                        t = i+1
                        t2 = j+1
        else:
            t = 0
            t2 = 0
print(t, t2)