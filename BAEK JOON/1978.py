a=int(input())
n = list(map(int, input().split()))[:a]
c=0
for i in n:
    if i<2:
        pass
    else:
        for j in range(2,i+1):
            if i%j==0:
                if j==i:
                    c += 1
                else:
                    break
print(c)
