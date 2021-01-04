num=int(input())
number=str(input())

number=number[:num]
number=list(map(int,number))

print(sum(number))
