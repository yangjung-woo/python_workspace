# 소수를 판별하는방법 
# 1. 무지성 N %1~k ==0 
# 2.N % 1~k/2 
# 3.N % 1~ 루트 k
def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):print(i)