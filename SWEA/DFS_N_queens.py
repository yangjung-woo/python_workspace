# NxN 보드판
def ispromising(col, level): # 해당 row level 에  z퀸을 둘수 있는가 판별 
    flag = True
    k = 1

    while(k<level and flag):
        if col[level]==col[k] or (abs(col[level]-col[k]) == level - k): # 대각선 혹은 같은 열에 존재하면 queen을 배치 불가 
            flag = False
        k+=1
    return flag

def N_queen_dfs(col,level):
    global case_num 
    N = len(col)-1
    if ispromising(col,level): # 현재 row level 에  퀸을 둘수 있다면 dfs 서칭 가능 
        if(level == N):
            case_num +=1
            #print(f'#{case_num}  {col[1:N+1]}')
            
        else:
            for j in range(1,N+1):
                col[level+1]= j
                N_queen_dfs(col,level+1)
    else:
        return

T = int(input())

for tc in range(1,1+T):
    N = int(input())
    case_num = 0
    col = [0]* (N+1)
    N_queen_dfs(col,0)
    print(f'#{tc} {case_num}')
