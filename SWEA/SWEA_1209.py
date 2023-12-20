# 1209. [S/W 문제해결 기본] 2일차 - Sum 

T = 10
N=100
for tc in range(1,1+T):
    ttc = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]

    sum_list = []
    # 모든 행 덧샘 추가 
    for i in range(N):
        row_total = sum(board[i][::])
        sum_list.append(row_total)
    # 모든 열 덧샘 추가 
    for j in range(N):
        col_list =[]
        for z in range(N):
            col_list.append(board[z][j])
        colum_total = sum(col_list)
        sum_list.append(colum_total)

    # 대각선 덧샘 추가 
    cross_list = []
    for k in range(N):
        cross_list.append(board[k][k])
    cross_total = sum(cross_list)
    sum_list.append(cross_total)

    # 대각선 덧셈 추가 2
    cross_list2 =[]
    for q in range(N):
        cross_list2.append(board[q][N-1-q])
    cross_total2 = sum(cross_list2)
    sum_list.append(cross_total2)
    print(f'#{ttc} {max(sum_list)} ')