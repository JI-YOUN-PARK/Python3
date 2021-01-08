cr=str(input())
crs=['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in crs:
    cr=cr.replace(i,"A")
print(len(cr))
