import sys
sys.setrecursionlimit(10**9)
N =int(sys.stdin.readline())
G =[[] for _ in range(N+1)]
dp = [[0,0] for i in range(N+1)]  # [일반,얼리어댑터]

for i in range(N-1):
    u,v = map(int,sys.stdin.readline().split())
    G[u].append(v)
    G[v].append(u)

visited = [False for i in range(N+1)]

def dfs(s):
    global G
    global visited
    visited[s] = True
    if len(G[s]) == 0: #s 에서 연결된 vertex 가 없을경우 
        dp[s][True] = 1 # s 가 얼리 어댑터인경우  최소 얼리어댑터수 1
        dp[s][False] = 0 #s 가 일반인 경우  최소 얼리어댑터수 0
    else:
        for i in G[s]:
            if visited[i] == False: # 아직 방문하지 않은경우 
                dfs(i)
                dp[s][1] += min(dp[i][0] , dp[i][1])
                dp[s][0] += dp[i][1]
        dp[s][1] += 1

def main():
    dfs(1)
    print(min(dp[1][0],dp[1][1]))


if __name__ == '__main__':
    main()





