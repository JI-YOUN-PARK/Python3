"""
@는 3을 곱하고
%는 5를 더하며
#는 7을 뺀다

첫째 줄에 테스트 케이스의 개수 T
둘째 줄에 화성 수학식
"""

a = int(input("테스트 케이스 개수 T입력 : "))
b=[]

for i in range(a):
    b=input("화성 수학식 입력 : ").split()
    c=len(b)
    f = float((b[0]))

    for j in range(1,c):
        n=b[j]
        if n =='@':
            f *=3
        elif n =='%':
            f +=5
        else:
            f -=7

print('%.2f' % f) # 소수점 2번째 자리까지 나타내기 위한 처리

