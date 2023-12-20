def prime_factorization(N):
    factors = {}
    i = 2
    while i * i <= N:
        while N % i == 0:
            factors[i] = factors.get(i, 0) + 1
            N //= i
        i += 1
    if N > 1:
        factors[N] = factors.get(N, 0) + 1
    return factors
 
 
T = int(input())
results =[]
for t in range(1,T+1):
    N= int(input())
    dict = prime_factorization(N)
    result = 1
    for key, value in dict.items():
        if(value%2!=0):
            result *=key
    results.append(result)
 
 
for i in range(0,T):
    print(f"#{i+1} {results[i]}")