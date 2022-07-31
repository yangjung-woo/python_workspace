import sys


def main():
    T = int(input())
    stairs =[0 for i in range(301)]
    dp = [0 for i in range(301)]
    for i in range(T):
        stairs[i]= int(input())
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])
    for i in range(3,T):
        dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])
    print(dp[T - 1])



if __name__ == '__main__':
    main()