T=int(input())
for i in range(T):
    k=int(input())
    n=int(input())

    home=[num for num in range(1,n+1)]

    for i in range(k):
        for j in range(1,n):
            home[j] += home[j-1]

    print(home[n-1])
