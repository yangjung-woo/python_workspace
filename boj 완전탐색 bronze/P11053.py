import sys


def main():
    N =int(input())
    lis = list(map(int,input().split()))
    dp =[0 for i in range(N)]
    for i in range(N):
        for j in range(i):
            if lis[i] > lis[j] and dp[i] < dp[j]:
                dp[i] = dp[j]
        dp[i] += 1
    print(max(dp))
       

if __name__ == '__main__':
    main()