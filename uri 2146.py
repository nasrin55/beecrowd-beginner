while True:
    try:
        n = int(input())
        password = n - 1
        print(password)

    except EOFError:
        break