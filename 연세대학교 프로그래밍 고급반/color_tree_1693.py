import sys
sys.setrecursionlimit(10**6) 
N = int(sys.stdin.readline())
G =[ [] for _ in range(N)]
visit = [False for _ in range(N)]
dp = [[0] * 16 for i in range(N)]
for i in range(N-1):
    u,v=map(int,sys.stdin.readline().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

def dfs(start):
        visit[start]= True
        for i in G[start]:
            if visit[i] == False:
                dfs(i)
                for pre_color in range(16):
                    Min_num =9999999
                    for color in range(16):
                        if pre_color != color:
                            if Min_num > dp[i][color]:
                                Min_num =dp[i][color]
                    dp[start][pre_color] += Min_num
        for color in range(16):
            dp[start][color] += color +1
        return


def main():
    
    dfs(0)
    print(min(dp[0]))



    


if __name__ == '__main__':
    main()
