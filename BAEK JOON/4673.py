def d(n):
    a=int(n)
    for i in list(str(n)):
        a=a+int(i)
    return a

self=[]
for j in range(10000):
    self.append(d(j))

for k in range(10000):
    if k in self:
        continue
    else:
        print(k)
