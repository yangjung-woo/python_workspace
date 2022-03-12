r1,c1,r2,c2 =list(map(int, input().split())) # 좌측 최상단1 우측 최하단2
dx =[1,0,-1,0]
dy =[0,1,0,-1]
board= [[0]* (c2-c1+1)for _ in range(r2-r1+1) ] #초기화
number_of_board = (c2-c1+1)*(r2-r1+1) #board 수 
y=x=0
num=1
cnt=0 #한 방향에서 움직이는 횟수
dcnt=1 # 한 방향에서 움직여야 하는 횟수
d=0

while number_of_board >0:
    if r1 <=y<= r2 and c1<=x<=c2:
        number_of_board-=1 
        board[y-r1][x-c1]=num
        max_num =num
    num +=1
    cnt +=1
    y=y+dy[d]
    x=x+dx[d]
    if cnt== dcnt: #같아질때 마다 0으로 초기화 
        cnt=0
        d=(d+3)%4  # 0-4
        if d==0 or d==2:
            dcnt+=1
max_num_len= len(str(max_num-1)) ##쵀개 길이만큼만 출력
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(board[i][j]).rjust(max_num_len),end=' ')
    print()