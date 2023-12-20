#5215. 햄버거 다이어트  D3
# DFS 문제 
# (단 여러 재료를 조합하였을 햄버거의 선호도는 조합된 재료들의 맛에 대한 점수의 합으로 결정되고, 
# 같은 재료를 여러 번 사용할 수 없으며, 햄버거의 조합의 제한은 칼로리를 제외하고는 없다.)
def dfs(index, sTaste, sKcal):
    global maxTaste
    
    # 총 칼로리를 넘으면 리턴
    if sKcal > L:
        return
        
    # taste의 합이 제일큰 taste 합보다 크면 갱신
    if maxTaste < sTaste:
        maxTaste = sTaste
        
    # 햄버거 재료 데이터를 다 돌면 리턴
    if index == N:
        return
        
    # index 파라미터를 통해 taste, kcal 대입
    taste, kcal = data[index]
    
    # 햄버거 재료 리스트에서 현재 재료(data[idx])를 사용했을 때
    dfs(index + 1, sTaste + taste, sKcal + kcal)
     # 현재 재료 미선택
    dfs(index + 1, sTaste, sKcal)
T = int(input())

for tc in range(1,1+T):

    N , L = map(int , input().split())

    data =  [list(map(int,input().split())) for _ in range(N)]

    maxTaste = 0
    dfs(0,0,0)
    print("#{} {}".format(tc, maxTaste))


