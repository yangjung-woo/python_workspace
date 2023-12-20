# 1215. [S/W 문제해결 기본] 3일차 - 회문1 D3


for tc in range(1,11):
    N = int(input())
    board = [list(input()) for _ in range(8)]
    count =0
    # 행 우선 탐색 
    for y in range(8):
        for x in range(8-N+1):
            A = board[y][x:x+N]
            if A[::] == A[::-1]:
                count += 1 
    # 열 탐색    각 열당  문자열의 첫번째 문자를 가져와서 B 로 만듬
    for y in range(8-N+1):
        for x in range(8):
            B=''
            for z in range(N):
                B += board[y+z][x] 
            if B[::] == B[::-1]:
                count += 1

    print(f'#{tc} {count}')