x=y=100

 

n=int(input("라운드 수 n:"))

for i in range(n):

    num=input()

    a, b=map(int, num.split(' '))

 

    if a > b:

        y -=a

    elif a < b:

        x -=b

 

 

print("x의 점수 :",x,"\ny의 점수:",y)
