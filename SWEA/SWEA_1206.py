# 빌딩 view 문제
# 창문을 열었을때 좌우 2칸 간격 이내에 공간이 확보되면 조망권이 확보됨 
for tc in range(1,11):
    total = 0
    N= int(input())
    building_height = list(map(int,input().split()))

    for i in range(2,N-2):
        diff1 = building_height[i] - building_height[i-2]
        diff2 = building_height[i] - building_height[i-1]
        diff3 = building_height[i] - building_height[i+1]
        diff4 = building_height[i] - building_height[i+2]
        if diff1 > 0 and diff2 > 0 and diff3 > 0 and diff4 > 0:
            total = total + min(diff1,diff2,diff3,diff4)
    print('#{} {}'.format(tc,total))