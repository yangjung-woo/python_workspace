# 격자판 숫자 이어 붙이기
# 완전탐색  DFS 문제 
def dfs(idx , row , col, string_num):
    dx = [1 ,-1 , 0 ,0 ]
    dy = [0, 0, -1 ,1]
    string_num = string_num + field[row][col]
    # 탈출 분기점 
    if idx == 6:
        result.append(string_num)
        return
    # 탈출이 아닐시 상하좌우 모든 이동 경우의수를 찾아 dfs 
    for i in range(4):
        if 0 <= row+dx[i]<4 and 0 <= col+dy[i]<4:
            dfs(idx+1, row+dx[i] ,col+dy[i] , string_num)

T= int(input())
for tc in range(1,1+T):
    field = [list(map(str,input().split())) for _ in range(4) ]
    result = [] # 결과값 저장 될 배열
    for x in range(4):
        for y in range(4):
            dfs(0,x,y,"")
 
    answer = set(result) # 중복 제거를 위해 set 사용
    print('#{} {}'.format(tc,len(answer)))