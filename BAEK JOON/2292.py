N=int(input())
total=1
start=1
go=6
if N==1:
    print(1)
else:
    while True:
        start+=go
        total+=1
        if N<=start:
            print(total)
            break
        go+=6
