n = int(input())

lst = list(map(int, input().split()))

min = lst[0]
count = 0
p = 0
for i in lst:
    if(i < min):
        min = i
        p = count
    count = count + 1
print('Menor valor: %d' %min)
print('Posicao: %d' %p)