N=int(input())
i = 2
while N!=1:         # N이 1이 되면 인수분해가 끝난 것이다.
    if N%i==0:      # N이 i로 나눠지는지 확인
        print(i)    # 나눠지면 i 출력
        N=N/i       # 그리고 N을 i로 나눈 값으로 N 업데이트
    else:
        i+=1        # 안 나눠떨어지면 인수가 아닌 것이므로 i에 1  더함
