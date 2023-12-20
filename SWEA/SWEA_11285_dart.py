# 다트 게임 
# 중심이 원점이고 반지름이 20,40,60,80,100,120,140,160,180,200 (단위는 mm)인 10개의 원이 그려져 있다.
#                       10 9  8  7  6   5   4   3   2   1    0  
# 반지름이 20 * (11 - p)인 경우 p점을 획득한다. (1 ≤ p ≤ 10)
# 220 - 20점수 = 반지름      =>  p = 11 - r/20
#만약 가장 큰 원 바깥에 꽂혔다면 얻는 점수는 없다.  200< 위치  는 점수가 없음
import math 
def calculate_point(x,y):
    r = math.ceil(math.sqrt(x*x + y*y)/20)
    if r ==0 :
        return 10
    elif r<=11:
        return 11-r
    else:
        return 0


T = int(input())

answer_list = []
for tc in range(1,1+T):
    N = int(input()) # 화살의 갯수 
    score = 0
    for i in range (N):
        x, y = map(int,input().split() )
        score += calculate_point(x,y)
    answer_list.append(score)
    #answer_list.append('#{} {}'.format(tc , answer)) ## 문자열을 100000개나 넣으니 스택 오버플로우가 발생하지 
for i in range(T):
    print(f"#{i+1} {answer_list[i]}")
