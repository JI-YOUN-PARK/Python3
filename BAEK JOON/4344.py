a=int(input())
count=0
list=[]
new_=[]
total=[]
for i in range(a):
    list=input()
    new=(list.split())
    new = [int (i) for i in new]
    avg = (sum(new) - new[0]) / new[0]

    for k in range(1, len(new)):
        if new[k] > avg:
            count = count + 1

    up = round((count / new[0]) * 100, 3)
    total.append(up)
    count=0

for l in range(a):
    print(format((total[l]),".3f")+"%")
