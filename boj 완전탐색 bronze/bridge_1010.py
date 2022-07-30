def main():
    T = int(input())
    for i in range(T):
        N ,M= map(int,input().split())
        dp = [[0 for i in range(M+1)] for i in range(N+1)]
    
        for j in range(1,N+1):
            for k in range(1,M+1):
                if j ==1:
                    dp[j][k] =k
                    continue
                if j == k:
                    dp[j][k] =1
                else:
                    if k >j:
                        dp[j][k] =dp[j][k-1]+dp[j-1][k-1]
        print(dp[N][M])


if __name__ == '__main__':
    main()