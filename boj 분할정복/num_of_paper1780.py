import sys
# NxN 크기의 종이 갯수 
N = int(sys.stdin.readline())
map_list = [list (map(int, input().split())) for _ in range(N)]
    #for _ in range(N):
    #    input = list(map(int, sys.stdin.readline().rstrip().split()))
    #    map_list.append(input)
cnt_of_min =0
cnt_of_zero =0
cnt_of_one =0

    
def dfs(x,y,N):
    global cnt_of_min ,cnt_of_zero,cnt_of_one
    num_check = map_list[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if (num_check != map_list[x][y]):
                for k in range(3):
                    for l in range(3):
                        dfs(x+k*N//3, y+l*N //3 ,N//3)
                return   
    # 9등분 반복후 각 map을 같은 종류의 숫자로만 이루어진 map_list 조사
     
    if num_check == -1:
        cnt_of_min += 1
    elif num_check == 0:
        cnt_of_zero += 1
    else:
        cnt_of_one += 1

dfs(0,0,N)
print(f'{cnt_of_min}\n{cnt_of_zero}\n{cnt_of_one}')

