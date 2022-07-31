import sys


def main():
    N = int(input())
    dp=[0,1,2]
    for i in range(3,N+1):
        insert = dp[i-1]+dp[i-2]
        dp.append(insert)
    print (dp[N] %10007)

if __name__ == '__main__':
    main()