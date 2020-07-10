def solution(strings, n):
    answer=[]
        
    answer=sorted(strings, key=lambda x : (x[n:n+1], x))
    
    return answer
