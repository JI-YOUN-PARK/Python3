word=input()
word=list(map(str,word))
total=[]
count=0
for k in range(0,26):
    total.append(-2)

for i in range(0,len(word)):
    num=ord(word[i])-97
    if total[num] != -2:
        count += 1
    else:
        total[num]=count
        count += 1

for j in range(0,26):
    if total[j]==-2:
        total[j]=-1
        print(total[j], end=' ')
    else:
        print(total[j], end=' ')
