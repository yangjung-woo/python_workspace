#16910. 원 안의 점 D3

# 격자점 : x, y 모두 정수인 점   의 갯수르 구하는 프로그램 작성
#  반지름 R 인 원안의 점 구성
# 원점 1개 , x축, y축 위에있는점들 r * 4 /  1234 좌표 평면 위에점 K *4
# K 를 구하는 방법  for i , j in range (1,N+1)  (x*x+ y*y) <= R*R 

T= int(input())

for tc in range(1,1+T):
    N = int(input())
    K = 0
    for x in range (1,1+N):
        for y in range(1,1+N):
            if x*x + y*y <=N*N:
                K= K+1
    
    answer = 1+ 4*N + K*4
    print(f"#{tc} {answer}")