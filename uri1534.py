while True:
    try:
        n = int(input())
        arr = []
        col = n - 1
        for i in range(n):
            tmp = []
            for j in range(n):
                if(j == col):
                    tmp.append(2)
                    col -= 1
                else:
                    if(i==j):
                        tmp.append(1)
                    else:
                        tmp.append(3)
            arr.append(tmp)
        for i in range(n):
            tx = ''
            for j in range(n):
                tx += str(arr[i][j])
            print(tx)
    except EOFError:
        break
