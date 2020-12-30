from collections import Counter
a=int(input())
b=int(input())
c=int(input())
for i in range(0,10):
    print(Counter(str(a*b*c))[str(i)])
