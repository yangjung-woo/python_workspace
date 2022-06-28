def dfs(start):
    if len(visit)==m:
        print(' '.join(map(str,visit)))
        return
    for i in range(start,n+1):
        if i not in visit:
            visit.append(i)
            dfs(i+1)
            visit.pop()

n,m=list(map(int,input().split())) # DFS 백트래킹을 사용하는 문제 
visit = [] # 방문기록


dfs(1)



