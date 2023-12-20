# 파리 퇴치 
# NxN 필드에서 mxm 영역만큼 공격했을때 가장 많은 파리를 잡을수 있게 해야함 

T = int(input())

for tc in range(1,T+1):
    N ,M = map(int,input().split())
    field = [[0]*N for _ in range(N) ] # NxN 필드 생성 
    for n in range(N):
        field[n] = list(map(int,input().split()))
    score = []
    for y_step in range(N-M+1):
        for x_step in range(N-M+1):
            sum_of_fly = 0
            for m_y in range(M):
                for m_x in range(M):
                    sum_of_fly += field[y_step+m_y][x_step+m_x]
            score.append(sum_of_fly)
    print('#{} {}'.format(tc, max(score)))
