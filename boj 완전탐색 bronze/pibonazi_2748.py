def main():
    N = int(input())
    dp = [0 for i in range(N+1)]
    dp[1]= 1
    for j in range(2,N+1):
        dp[j]=dp[j-1] +dp[j-2]
    print(dp[N])

if __name__ == '__main__':
    main()