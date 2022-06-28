a,b,c,n =map(int, input().split())
dp=[0] * 301
dp[a]=dp[b]=dp[c]=1
# dp[x]= 1 이면 dp[x+a] dp[x+b] dp[x+c] 가능 
# dp[x-a]  dp[x-b]  dp[x-c]셋중 하나라도 1 이면  dp[x]=1
# dp[2] =1    dp[2+2] , dp[2+3]  , dp [2+5] 도 가능   : 2 3 5 인실사용시  4 5 7 명 수용 가능함 즉 모든 학생을 수용할수 있음
for i in range(a,n+1):
    for j in [a,b,c]:
            if i >= j and dp[i-j]:
               dp[i]=1
print(dp[n]) 