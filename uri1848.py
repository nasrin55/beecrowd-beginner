sum = 0
arr = []
for i in range(3):
    sum = 0
    while(1):
        arr = input()
        arr = str(arr)
        if(arr[0] == 'c'):
            break
        if(arr[0] == '-'):
            if(arr[1] == '-'):
                if(arr[2] == '-'):
                    sum += 0
                else:
                    sum += 1
            else:
                if (arr[2] == '-'):
                    sum += 2
                else:
                    sum += 3


        elif(arr[0]== '*'):
            if(arr[1] == '-'):
                if(arr[2] == '-'):
                    sum += 4
                else:
                    sum += 5
            else:
                if (arr[2] == '-'):
                    sum += 6
                else:
                    sum += 7

    print(sum)
