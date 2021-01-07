num=input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
total=0
for i in range(len(num)):
    for j in dial:
        if num[i] in j:
            total += dial.index(j)+3
print(total)
