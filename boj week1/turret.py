import math

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 두 원의 거리 (원의방정식활용)
    if distance == 0 and r1 == r2 :  # 두 원이 동심원이고 반지름이 같을 때 점이 무한대
        print(-1) 
    elif abs(r1-r2) == distance or r1 + r2 == distance:  # 내접, 외접일 때 절대값
        print(1)
    elif abs(r1-r2) < distance < (r1+r2) :  # 두 원이 서로다른 두 점에서 만날 때
        print(2)
    else:
        print(0)  # 
        # 원의 방정식 문제 만나는점 0 1 2  3개의 case를 구현하는 간단문제