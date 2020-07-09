yes=0
no=0

a=int(input("설문조사를 한 사람의 수 : "))

for i in range(a):
    b=input("의견을 입력 : ")

    if b == '0':
        no = no + 1
    else:
        yes = yes +1


if no < yes :
    print("cute")

else :
    print("not cute")
