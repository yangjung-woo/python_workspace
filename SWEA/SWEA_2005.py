# 2005. 파스칼의 삼각형 D2

T = int(input())

for tc in range(1,1+T):
    N = int(input())
    answer = [[0 for _ in range(1,h+1)] for h in range(1,N+1)]
    answer[0][0] = 1
    if N >=2:
        answer[1][0] = 1
        answer[1][1] =1
    for i in range(2,N):
        answer[i][0] = 1
        for j in range(1,i): # 각 level 양 끝은 포함하지 않음 
            answer[i][j]= answer[i-1][j-1]+answer[i-1][j]
        answer[i][-1] = 1
    print(f'#{tc}')
    for k in answer:
        print(*k)
    answer = []
