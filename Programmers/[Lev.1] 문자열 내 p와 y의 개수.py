def solution(s):
    word=''
    word=s.lower()

    sum1 = word.count('p')
    sum2 = word.count('y')

    if sum1 == sum2:
        answer = True
    else:
        answer = False
        
    return answer
