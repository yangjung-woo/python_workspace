# 프로그래머스 정수 삼각형 문제
# 위에서 아래로 내려가는 정수 삼각형 중 
# 거쳐간 정수의 합이 최대가 되도록 출력하는 프로그램 작성 

# way: Dp ,
def solution_DP(triangle):
    n = len(triangle)
    DP =[[0 for i in range(h+1)] for h in range(n)]# len(dp) =5  인 최대값만 들어가는 DP
    
    DP[0][0] = triangle[0][0]
    for i in range(1,n):
        DP[i][0]= DP[i-1][0] + triangle[i][0]
        for j in range(1,i):
            DP[i][j] = max(DP[i-1][j] , DP[i-1][j-1])+triangle[i][j]
        DP[i][-1]= DP[i-1][-1] + triangle[i][-1]
    return max(DP[-1])


A= [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5] ]
print(solution_DP(A))
