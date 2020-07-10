def solution(a, b):
    answer = 0
    c=0
    
    if a>b:
        c=a
        a=b
        b=c
        
    for a in range(a,b+1):
        answer=answer+a
    
    return answer
