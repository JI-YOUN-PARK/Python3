a=input().lower()
b=list(set(a))
total=[]
for i in b:
    c=a.count(i)
    total.append(c)

if total.count(max(total)) >= 2:
    print("?")
else:
    print(b[total.index(max(total))].upper())
