num=[0,1]
i=int(input())
for j in range(i-1):
    num.append(num[j]+num[j+1])

print(num[i])
