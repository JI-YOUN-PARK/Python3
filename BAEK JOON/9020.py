def prime(n):
    s=[True]*n
    m = int(n**0.5)
    for i in range(2,m+1):
        if s[i]==True:
            for j in range(i+i,n,i):
                s[j]=False
    return [i for i in range(2,n) if s[i]==True]

def sosu(n):
    l=prime(n)
    idx=max([i for i in range(len(l)) if l[i]<=n/2])
    for i in range(idx,-1,-1):
        for j in range(i,len(l)):
            if l[i]+l[j]==n:
                return [l[i],l[j]]

for _ in range(int(input())):
    n=int(input())
    print(" ".join(map(str,sosu(n))))
