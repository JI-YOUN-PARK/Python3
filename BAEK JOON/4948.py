N = 123456 * 2 + 1  #각 테스트 케이스에 대해서, n보다 크고, <2n보다 작거나 같은> 소수의 개수를 출력
sieve = [True] * N  # True인 list를 N개만큼 생성한다
for i in range(2, int(N**0.5)+1):   #소수 개수 체크할 때 N의 반까지만 체크하면 됨
    if sieve[i]:
        for j in range(2*i, N, i):  #i의 배수(i가 2라면 j=4,6,8,10...)을 제외시킨다.
            sieve[j] = False

def prime_cnt(val):
    cnt = 0
    for i in range(val + 1, val * 2 + 1):
        if sieve[i]:  #if sieve[i] is True
            cnt += 1
    print(cnt)

while True:
    val = int(input())
    if val == 0:
        break
    prime_cnt(val)
