# 달팽이 숫자 
T = int(input())

for tc in range(1,T+1):
    N= int(input())
    dx =[0 ,1, 0 , -1]
    dy =[1, 0, -1, 0]
    snail = [[0]*N for _ in range(N)]
    x , y = 0 ,0 # 초기위치 ,
    #회전방향   0 1 2 3   : 우 하 좌 상
    dist = 0
    for n in range(1,N*N+1):
        snail[x][y] =n
        x += dx[dist]
        y += dy[dist]

        # 범위를 벗어나거나 0이 아닌 값이 이미 있다면 dist 방향 전환
        if x<0 or y<0 or x>=N or y>=N or snail[x][y]!=0:
            # 진행 취소 
            x -= dx[dist]
            y -= dy[dist]

            dist = (dist+1) % 4

            x += dx[dist]
            y += dy[dist]    
    print('#{}'.format(tc))
    for row in snail:
      print(*row)