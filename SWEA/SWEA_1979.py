# 어디에 단어가 들어갈 수 있을까? 


T = int(input())

for tc in range(1,1+T):
    N , k = map(int,input().split())
    field = [list(map(int,input().split()))  for _ in range(N)]
    answer = 0
    for i in range(N):#행 단위 탐색 
        cnt =0
        for j in range(N): 
            if field[i][j]==1:
                cnt = cnt+1
            if field[i][j] ==0 or j == N-1:
                if cnt == k:
                    answer +=1
                cnt = 0
    for i in range(N):#열 단위 탐색 
        for j in range(N): 
            if field[j][i]==1:
                cnt = cnt+1
            if field[j][i] ==0 or j == N-1:
                if cnt == k:
                    answer +=1
                cnt = 0


    print('#{} {}'.format(tc,answer))