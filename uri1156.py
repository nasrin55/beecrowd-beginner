s = 0
n = 1
for i in range(1,40,2):
    s = s + i/n
    n = n*2
print('%.2f' %s)