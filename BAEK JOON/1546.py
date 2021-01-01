n=int(input())
a=list(map(int,input().split()))
a=a[:n]
m=max(a)
t=0
for i in range(len(a)):
    a[i]=a[i]/m*100
    t=t+a[i]
print(t/n)
