import sys


def main():
    N ,target = map(int, sys.stdin.readline().split())
    coin=[]
    dp = [0 for _ in range(target+1)] 
    dp[0] = 1
    for _ in range(N):
        insert = int(input())
        coin.append(insert)

    for i in coin:
        for j in range(i,target+1):
            if j>= i:
                dp[j] += dp[j-i]

    print(dp[target])    

if __name__ == '__main__':
    main()