N=int(input())
cnt=0
chess_board=[[0 for col in range(N)] for raw in range(N)]  # 0 able 1: cant 2 :queen
def queen(y,x,size):
    for i in range(0,size): # x열 전부 설치불가
        if(chess_board[i][x]==0):chess_board[i][x] =1
    for j in range(0,size):# y열 전부 설치불가
        if(chess_board[y][j]==0):chess_board[y][j] =1
    for k in range(0,size):# 대각선 전부 설치불가
        for l in range(0,size):
            if abs(y-k)==abs(x-l):
                chess_board[k][l]==1

def factorial(x):
    if(x>1): return x*factorial(x-1)
    else:return 1


for i in range(N):
    for j in range(N):
        if chess_board[i][j]==0:
            chess_board[i][j] == 2 # 퀸 배치
            cnt+=1
            queen(i,j,N)
print(cnt)