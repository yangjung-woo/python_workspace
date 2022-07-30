import sys


def main():
    N ,target = map(int, sys.stdin.readline().split())
    coin=[]
    dp = [10001 for _ in range(target+1)] 
    dp[0] =0
    for _ in range(N):
        insert = int(input())
        coin.append(insert)

    for i in coin:
        for j in range(i,target+1):
            dp[j]=min(dp[j],dp[j-i]+1)
    if dp[target] ==10001:
        print("-1")
    else:print(dp[target])    

if __name__ == '__main__':
    main()