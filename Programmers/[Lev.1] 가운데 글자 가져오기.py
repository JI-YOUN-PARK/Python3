def solution(s):
    a = len(s)
    answer = ''

    if a % 2 == 1:
        b = a // 2
        answer = s[b]
    else:
        b = a // 2
        for b in range(b-1, b + 1):
            answer = answer + s[b]
            
    return answer
