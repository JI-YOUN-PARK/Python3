def solution(array, commands):
    answer = []
    
    for text in commands:
        i,j,k=text[0],text[1],text[2]
        list=array[i-1:j]
        list.sort()
        answer.append(list[k-1])
    return answer
