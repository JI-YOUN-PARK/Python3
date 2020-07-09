v=int(input("심사위원의 수 : "))
total = input("투표하세요! : ")
#v를 입력받아 v개 만큼 수를 입력하고자 했는데, python에 그런 코드는 없다고 한다.

a=total.count("A")
b=total.count("B")

print('A' if a>b else 'B' if b>a else 'SAME')
