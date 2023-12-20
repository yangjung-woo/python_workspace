# N - queen 문제 


def adjacent(next_level):  # x와 i 가 같으면 행이 같은거 근데 for문을 보면 x와 i가 같을 수가 없다.
    for i in range(next_level):  # 인덱스가 행  row[n]값이 열
        if row[next_level] == row[i] or abs(row[next_level] - row[i]) == next_level - i:  # 열이 같거나 대각선이 같으면 false
            return False  # 대각선이 같은경우는 두 좌표에서 행 - 행 = 열 - 열 이 같으면 두개는 같은 대각선상에 있다.
    return True


# 한줄씩 재귀하며 dfs 실행

def dfs(level , row , N):
    global result

    if level == N:# 마지막 point 이면 종료
        result += 1
        
    else:
        # 각 행에 퀸 놓기
        for i in range(N):  # i 는 열번호 0부터 N 전까지 옮겨가면서 유망한곳 찾기
            row[level] = i
            if adjacent(level):  # 행,열,대각선 체크함수 true이면 백트래킹 안하고 계속 진행
                dfs(level + 1, row ,N)

T = int(input())
for tc in range(1, T+1):
 
    N = int(input()) # Queen 의 갯수 및 NxN 체스판 
    row = [0] * N
    result = 0
  
    dfs(0,row,N)

    print(f'#{tc} {result}')