a,b,k = input().split()
a = int(a)
b = int(b)
k = int(k)

if a%k == 0 and b%k == 0:
    print('Both')
if a%k == 0 and b%k != 0:
    print('Memo')
if a%k != 0 and b%k == 0:
    print('Momo')
if a%k != 0 and b%k != 0:
    print('No One')

