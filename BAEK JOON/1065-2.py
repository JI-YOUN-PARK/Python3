def han(N):
    if N<100:
        t=N
    else:
        t=99
        for i in range(100,N+1):
            n=list(map(int,str(i)))
            if (n[0]-n[1]) == (n[1]-n[2]):
                t = t+1
    return (t)

c=int(input())
d=han(c)
print(d)
