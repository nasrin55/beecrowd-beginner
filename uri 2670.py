floor = [int(input()) for i in range(3)]
time = []
time.append(floor[0]*4 + floor[1]*2)
time.append(floor[0]*2 + floor[2]*2)
time.append(floor[1]*2 + floor[2]*4)

time.sort()
print(time[0])