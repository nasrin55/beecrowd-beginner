N=int(input())
for i in range(N):
    soma = 1
    X=int(input())
    for t in range(2,X):
        if(X%t==0):
            soma = 0
    if (soma):
        print(X, "eh primo")
    else:
        print(X, "nao eh primo")