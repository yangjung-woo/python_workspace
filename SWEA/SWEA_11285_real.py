import math
result = []
TC = int(input())
for test_case in range(1,TC+1):
    N = int(input())
    score = 0
    for _ in range(N):
        x,y = map(int,input().split())
        r = math.ceil(math.sqrt(x*x + y*y)/20)
        if r== 0:
            score += 10
        elif r <= 11:
            score += (11-r)
    result.append(score)  
for i in range(TC):
    print(f"#{i+1} {result[i]}")