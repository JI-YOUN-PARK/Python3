"""
1번 입력 :  현재 시각
            시 A (0<=A<=23) 와 분 B (0<=B<=59)가 정수로 빈칸을 사이에 두고
            순서대로 주어짐

2번 입력 : 요리하는 데 필요한 시간 C (0<=C<=1,000)가 분 단위로 주어짐. 
"""
a,b=input("시각 A와 분 B를 공백을 두고 입력 : ").split()
a=int(a)
b=int(b)

c = int(input("걸린 시간 C를 입력 : "))

n=(b+c)//60  # 일단 분에 해당되는 B와 C를 더한다. 그 후, //60 을 통해 몫을 구한다.
             # 이 몫은 60분을 초과한 '시'에 해당되므로, 이 값을 차후에 A에 더한다.
m=(b+c)%60   # //60을 하여 '시'를 계산한 후에 분을 계산한다.

a+=n         # 위에서 말한 '차후에 A에 더한다'는 부분에 해당한다.

print(a,"   ",m)

