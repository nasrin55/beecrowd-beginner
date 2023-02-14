date = input()
d = date[:2]
m = date[3:5]
y = date[6:]

print('{}/{}/{}'.format(m,d,y))
print('{}/{}/{}'.format(y,m,d))
print('{}-{}-{}'.format(d,m,y))
