def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):  # num 루트까지 확인했을때 루트기준으로 양쪽 대칭 즉 왼쪽에서 소수가 아니다!  오른쪽 안봐도됌
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)