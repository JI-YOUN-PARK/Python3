a=int(input())
new=[]
last=[]
other=''
for i in range(a):
    b=list(map(str,input()))

    rept=int(b[0])
    new=b[2:int(len(b))]

    for j in range(len(new)):
        for k in range(rept):
            other=other+str(new[j])
    last.append(other)
    other=''

print('\n'.join(last))
