# 햄버거 다이어트 
# 햄버거의 맛은 최대한 유지하면서 정해진 칼로리를 넘지 않는 햄버거를 주문하여 먹으려고 한다.
# 이 가게에서 자신이 먹었던 햄버거의 재료에 대한 맛을 자신의 오랜 경험을 통해 점수를 매겨놓았다.

#민기가 좋아하는 햄버거를 먹으면서도 다이어트에 성공할 수 있도록 정해진 칼로리 이하의 조합 중에서 민기가 가장 선호하는 햄버거를 조합해주는 프로그램을 만들어보자.
#(단 여러 재료를 조합하였을 햄버거의 선호도는 조합된 재료들의 맛에 대한 점수의 합으로 결정되고, 같은 재료를 여러 번 사용할 수 없으며, 햄버거의 조합의 제한은 칼로리를 제외하고는 없다.)

# 동적 프로그래밍 문제 , 배낭 체우기 알고리즘 

T = int(input())
for tc in range(1,1+T):
    dic ={}
    dic_nomalized = {}
    N,L = map(int , input().split())# N 은 재료의 갯수 , L은 제한 칼로리 
    for _ in range(N):
        point , cal = map(int,input().split())
        dic[point] = cal # 딕셔너리는 append 를 사용할 수가 없다 대신 dic[key] =value 를 통해 넣을수 있음 
        dic_nomalized[point] = int(point / cal)
    select_point =0
    select_cal =0
    answer = 0
    while L>=0:
        for poi , ca in dic.items():  # 딕셔너리에서 뽑아오기 위해선 dic.item()
            if (ca > L):
                dic.pop(poi)
                dic_nomalized.pop(poi) # 현재 칼로리를 넘는 재료는 제거한다 
        
        select_point = max(dic_nomalized, key=dic_nomalized.get) # 딕셔너리에서 value가 최대를 갖는 key를 찾기 
        select_cal = dic[select_point]
        
        # 갱신 
        L = L -select_cal
        answer += select_point
    print(f"#{tc} {answer}")
