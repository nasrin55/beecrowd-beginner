from math import sqrt

def accuracy(qt, list, mean):
    summation = 0
    for i in range(qt):
        summation += (list[i] - mean)**2
    result = sqrt( (summation) / (qt - 1) )
    return result

while True:
    try:

        h,m = input().split()
        values = [float(x) for x in input().split()]
        case = (int(h) * 60) // int(m)
        mean = sum(values) / case
        result = accuracy(case, values, mean)

        print('%.5f' %result)

    except EOFError:
        break