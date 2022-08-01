import sys


def main():
    T = int(input())
    
    for i in range(T):
        N = int(input())
        coin = list(map(int, sys.stdin.readline().split()))
        target = int(input())
    
        dp=[0 for i in range (target+1)]
        dp[0]=1
        for j in coin:
            for k in range (target+1):
                if k>=j:
                    dp[k] = dp[k] +dp[k-j]
        print(dp[target])
if __name__ == '__main__':
    main()