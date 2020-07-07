def solution(answers):   
    s1=[1,2,3,4,5]
    s2=[2,1,2,3,2,4,2,5]
    s3=[3,3,1,1,2,2,4,4,5,5]
    
    a1=0
    a2=0
    a3=0
    
    for i in range(len(answers)):
        if answers[i]==s1[i%5]:
            a1 += 1
        if answers[i]==s2[i%8]:
            a2 += 1
        if answers[i]==s3[i%10]:
            a3 += 1
    max1=max(a1,a2)
    max1=max(max1,a3)
    
    answer = []
    
    if max1 == a1:
        answer.append(1)
    if max1 == a2:
        answer.append(2)
    if max1 == a3:
        answer.append(3)
    return answer
    answer = []
    return answer
