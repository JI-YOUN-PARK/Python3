from sys import stdin

v = int(input("심사위원의 수를 입력 : "))
list1 = input("투표하세요! : ")

list2 = list1[0:v]

a=list2.count("A")
b=list2.count("B")


print(list2+"에서 계산합니다.")
print('A' if a>b else 'B' if b>a else 'SAME')



