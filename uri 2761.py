e = input().split()
a = int(e[0])
b = float(e[1])
c = e[2]
d = ' '.join(e[3:])
t = ''.join(e)
print('%s' % t)
print('%d\t%f\t%c\t%s' %(a,b,c,d))
print('%10d%10f%10c%10s' %(a,b,c,d))