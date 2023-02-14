tourist = 0
jeep = 0

while True:
    entry = input().split()
    if entry[0] == 'ABEND':
        break
    if entry[0] == 'SALIDA':
        jeep += 1
        tourist += int(entry[1])
    else:
        jeep -= 1
        tourist -= int(entry[1])

print(tourist)
print(jeep)
