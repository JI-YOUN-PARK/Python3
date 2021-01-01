num=int(input())
quiz=[]
total=0
last=[]
for i in range(num):
    quiz.append(input())

for i in range(num):
    c=1
    answer=list(quiz[i])
    if answer[0]=='X':
        total=0
    else:
        total=1

    for j in range(1, len(answer)):
        if answer[j]=='O' and answer[j-1]=='O':
            c=c+1
            total=total+c
        elif answer[j]=='O' and answer[j-1]=='X':
            total=total+1
        else:
            c=1
    last.append(total)

for k in range(num):
    print(last[k])
