# 덤프 문제 최대 높이와 최소 높이 간 차이를 출력
# list.index(값):  값 이 있는 위치를 반환함 

#
T = 10

for tc in range(1,1+T):
    N= int(input())
    heights = list(map(int,input().split()))
    for i in range(N): # 덤프 수 만큼 평탄화
        heights[heights.index(max(heights))] -= 1 # 최댓값 +1
        heights[heights.index(min(heights))] += 1 # 최솟값 -1
        #max_height = max(heights)
        #min_height = min(heights)
        #heights[heights.index(max_height)] -= 1
        #heights[heights.index(min_height)] += 1
    answer  = max(heights) - min(heights)
    print('#{} {}'.format(tc,answer)) 

    