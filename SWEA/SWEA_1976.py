# 1976. 시각 덧셈 D2 

T = int(input())


for tc in range(1,1+T):

    h1, m1 ,h2 , m2 = map(int,input().split())
    total_m = (m1 + m2)%60
    upper_h = (m1 +m2)//60

    total_h = (h1+h2+upper_h)
    if total_h >12:  # 시간은 1~ 12 사이 이므로  %12 : 0~11 올바르지 않다 
        total_h -= 12

    print(f'#{tc} {total_h} {total_m}')