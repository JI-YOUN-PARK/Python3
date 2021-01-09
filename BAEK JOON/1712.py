a,b,c=list(map(int,input().split()))
x=0
if(c<=b):
    x=-1
else:
    x=a//(c-b)+1
print(x)
