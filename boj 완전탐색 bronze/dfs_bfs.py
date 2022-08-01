from collections import deque
import sys
N,M,start = map(int,sys.stdin.readline().split())
G=[[0]*(N+1)  for _ in range(N+1)]
visit_bfs=[False for _ in range(N+1)]
visit_dfs=[False for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    G[u][v] = G[v][u] =1

def dfs(now):
        visit_dfs[now]= True
        print(now,end=" ")
        for i in range(1,N+1):
            if G[now][i]==1 and visit_dfs[i] == False:
                dfs(i) 

def bfs(now):
        q=deque()
        q.append(now)       
        visit_bfs[now] = 1   
        while q:
            now = q.popleft()
            print(now, end = " ")
            for i in range(1, N + 1):
                if visit_bfs[i] == False and G[now][i] == 1:
                    q.append(i)
                    visit_bfs[i] = 1    

def main():
    
    
    dfs(start)
    print()
    bfs(start)
    



    


if __name__ == '__main__':
    main()