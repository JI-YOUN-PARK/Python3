num = int(input())

for i in range(num):
    H, W, N = map(int, input().split())
    line = N // H + 1

    if N % H == 0:
        floor = H
        line = N // H
    else:
        floor = N % H

    answer = floor * pow(10, 2) + line
    print(answer)
