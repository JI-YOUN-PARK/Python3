def solution(arr):
    answer = []
    
    for i in range(0,len(arr)):
        if i==len(arr)-1:
            answer.append(arr[i])
        else:
            if arr[i] != arr[i+1]:
                answer.append(arr[i])
    return answer
