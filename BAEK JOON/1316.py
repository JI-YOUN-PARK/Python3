t = int(input())
group = 0

for i in range(t):
    gp = input()
    cnt = 0    
    for j in range(len(gp)-1):
        if gp[j] != gp[j+1]:
                new = gp[j+1:]
                if new.count(gp[j]) > 0:
                    cnt += 1
    if cnt == 0:
        group += 1
print(group)   
