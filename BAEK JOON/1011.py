num=int(input())

for i in range(num):
    x, y = list(map(int, input().split()))
    total=y-x
    count=0
    go=1
    go_sum=0
    while total>go_sum:
        count+=1
        go_sum+=go
        if count%2==0:
            go+=1
    print(count)
