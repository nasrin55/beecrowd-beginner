n = int(input())
for i in range(n):
   lista = [int(num) for num in input().split()]
   x = min(lista)
   y = max(lista)
   sum = 0
   for num in range(x + 1, y):
       if (num % 2 == 1):
           sum = sum + num
   print(sum)