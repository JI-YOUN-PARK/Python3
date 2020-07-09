def solution(a, b):
    sum=0
    month=[31,29,31,30,31,30,31,31,30,31,30,31] 
    day=['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    if a==1:
        sum=(sum+b-1)%7
    else:
        for i in range(0,a-1):
            sum =sum+month[i]
            
        sum=(sum+b-1)%7
    answer=day[sum]
    return answer
