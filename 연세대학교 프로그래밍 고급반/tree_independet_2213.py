import sys

sys.setrecursionlimit(10**9)
N =int(sys.stdin.readline())
weigt_list =[0]+ list(map(int,sys.stdin.readline().split()))
dp = [[0]*2 for i in range(N+1)]  # [자신 포함시 가중치 합, 자신 포함 안할 시 가중치 합]

G =[[] for _ in range(N+1)]



visited = [False for i in range(N+1)]
S =[[[],[]]for i in range(N+1)]    # 자기 자신 포함시 집합 S 리스트 , 자기자신 비 포함시 집합 S 리스트

def dfs(start):
    #start 정점을 S 에 포함하고 방문할 경우
    visited[start] = True
    dp[start][0] = weigt_list[start]
    S[start][0].append(start)

    for i in G[start]:
        if not visited[i]:
            dfs(i)
            dp[start][0] += dp[i][1]
            for j in S[i][1]:
                S[start][0].append(j)
            if max(dp[i][1],dp[i][0]) ==dp[i][1]:
                dp[start][1]+=dp[i][1]
                for k in S[i][1]:
                    S[start][1].append(k)
            else:
                dp[start][1] += dp[i][0]
                for k in S[i][0]:
                    S[start][1].append(k)
                    
for i in range(N-1):
    u,v = map(int,sys.stdin.readline().split())
    G[u].append(v)
    G[v].append(u)    

def main():
    dfs(1)
    if max(dp[1][0], dp[1][1]) == dp[1][0]:
        print(dp[1][0])
        a = S[1][0]
        a.sort()
        print(*a)
    else:
        print(dp[1][1])
        a = S[1][1]
        a.sort()
        print(*a)


if __name__ == '__main__':
    main()