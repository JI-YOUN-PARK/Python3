M=int(input())
N=int(input())
last=[]

for i in range(M,N+1):
    if i<2:
        pass
    else:
        for j in range(2,i+1):
            if i%j==0:
                if j==i:
                    last.append(j)
                else:
                    break
if not last:
    print(-1)
else:
    print(sum(last))
    print(min(last))
