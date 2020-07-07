test={}

school=[]

 

t=int(input("테스트 케이스 숫자 T:"))

for i in range(0,t):

    n=int(input("학교의 숫자 정수 N:"))

    

    for j in range(0,n):

        a=input()

        b=int(a.find(' '))

        c=a[:b]

        d=a[b:]

        test[c]=d

        maximum=max(test.values())

        

    for s,v in test.items():

        if v == maximum:

            school.append(s)

 

print(school)
