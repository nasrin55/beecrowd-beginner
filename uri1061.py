d = input().split()
w = int(d[1])
h = input().split()
x = int(h[0])
y = int(h[2])
z = int(h[4])

d1 = input().split()
w1 = int(d1[1])
h1 = input().split()
x1 = int(h1[0])
y1 = int(h1[2])
z1 = int(h1[4])

days = w1 - w
hours = x1 - x
mint = y1 - y
sec = z1 - z
if(sec < 0):
    sec = 60 + sec
    mint = mint - 1

if(mint < 0):
    mint = 60 + mint
    hours = hours - 1

if(hours < 0):
    hours = 24 + hours
    days = days - 1

if(days <= 0):
    day = 0

print('%i dia(s)' %days)
print('%i hora(s)' %hours)
print('%i minuto(s)' %mint)
print('%i segundo(s)' %sec)