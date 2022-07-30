
def main():
    N = int(input())
    dp =[0 for i in range(N+1)]
    dp[1]=1
   
    for i in range(2,N+1):
        min_value = 1e9 
        j=1
        while (j**2) <= i:
            min_value = min(min_value, dp[i - (j**2)])
            j += 1
        dp[i]= min_value+1
    print(dp[N])





if __name__ == '__main__':
    main()