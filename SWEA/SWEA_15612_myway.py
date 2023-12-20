# 체스판 위에 록 배치하기
# 8x8 모든  행과 열에는 단 1개의 록만 존재해야 한다 
# 즉 row =[1,1,1,1,1,1,1,1]
#    col = [1,1,1,1,1,1,1,1] 임을 만족해야 함 
T = int(input())

for tc in range(1,1+T):
    board = []
    for i in range(8):
        line = list(input())
        board.append(line)
    # 8x8 board 생성 완료 
    row = [0]*8
    col = [0]*8

    for y in range(8):
        for x in range(8):
            if board[y][x]=='O':
                row[x] +=1
                col[y] +=1
    
    answer = "yes"
    for y in range(8):
        if col[y] !=1:
            answer = "no"   
    for x in range(8):
        if row[x] !=1:
            answer = "no"  

    print(f"#{tc} {answer}")