import sys


def main():
    N = int(input())
    dp=[0,1,3]
    for i in range(3,N+1):
        insert =(dp[i-2]*2) + dp[i-1]
        dp.append(insert)
    print (dp[N] %10007)

if __name__ == '__main__':
    main()