n = int(input())

dp = [0] * (n+1) # 모든 가능성을 저장할 dp[k]
# k=>1 동안 필요한 계산수를 저장 ->  dp[2] = 2-1 (1번) =1

for i in range(2, n+1): #2 ~ n
    dp[i] = dp[i-1] + 1 # dp 0 1 2 3 4 5 6 ...n   -1한 경우의수만 dp에 저장 

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)  # -1 경우보다 /2의 경우수가 더 작으면 수정 
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)# -1 경우보다 /3의 경우수가 더 작으면 수정

print(dp[n])


# 땡! DP 동적 계획법 이전의 자료를 이용 
# cnt =0
# n =int(input())
# while(n!=1):
#     if n%3==0:
#         n=n/3
#         cnt+=1
#     elif n%2==0:
#         n=n/2
#         cnt+=1
#     else:
#         n-=1
#         cnt+=1
# print(cnt)

