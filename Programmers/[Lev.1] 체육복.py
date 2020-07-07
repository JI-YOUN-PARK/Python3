def solution(n, lost, reserve):
    list = []
    re=[]
    answer = 0
    for i in range(n):
        list.insert(i, 1)

    for i in range(len(lost)):
        b = lost[i]
        list[b-1]=0

    for i in range(len(reserve)):
        c=reserve[i]
        list[c-1]=2

    for i in reserve:
        if i not in lost:
            re.append(i)

    for i in range(len(re)):
        a=re[i]
        if list[a-1] == 2:
            if a !=1 and a != n:
                if list[a - 2] == 0:
                    list[a - 2] = 1
                    list[a-1] = 1
                if list[a-1]==2:
                    if list[a] == 0:
                        list[a] = 1
                        list[a-1] = 1
            elif a == 1:
                if list[a] == 0:
                    list[a] = 1
                    list[a-1] = 1
            elif a == n:
                if list[a - 2] == 0:
                    list[a - 2] = 1
                    list[a-1] = 1
    for i in range(n):
        if list[i]==2:
            list[i]=1

    for i in range(0, n):
        x = list[i]
        if x == 1:
            answer = answer + 1
            
    return answer
