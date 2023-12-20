# 농작물 수확하기 문제 
#N X N크기의 농장이 있다.
#이 농장에는 이상한 규칙이 있다.
#규칙은 다음과 같다.
#  ① 농장은 크기는 항상 홀수이다. (1 X 1, 3 X 3 … 49 X 49)
#  ② 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능하다.
T = int(input())

for tc in range(1,1+T):
    N= int(input()) # 단 N 은 반드시 홀수 

    field = [list(map(int,input())) for _ in range(N)] ## list(string) 은 한 문자씩 잘라서 리스트에 저장    
    # list(map(int,input().split()))  띄어쓰기씩 나눠서 int 로 매핑한후 리스트로 저장 
    #print(field)
    # front sum 
    total = 0
    for i in range(N//2):
        #print((field[i][N//2-i : N//2+i+1]))
        total = total + sum(field[i][(N//2)-i : (N//2)+i+1])
    # middle sum
    total = total +sum(field[N//2][::])
    # post sum
    for j in range(N//2+1 , N):
        #print((field[j][N//2-(N-j-1) : N//2+(N-j-1)+1]))
        total = total +sum(field[j][(N//2) - (N-j-1) :(N//2) + (N-j-1)+1])

    print('#{} {}'.format(tc,total))