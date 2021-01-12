N = int(input())
b3 = 0
b5 = N//5
N %= 5

while b5 >=0:
    if N % 3 ==0:
        b3 = N//3
        N %= 3;
        break
    b5 -= 1
    N += 5
print(N==0 and (b3 + b5) or -1)
