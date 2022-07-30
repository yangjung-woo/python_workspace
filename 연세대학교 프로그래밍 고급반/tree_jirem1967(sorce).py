import sys
sys.setrecursionlimit(10**5)

# 연결된 vertex 집합중에 트리에서 가장 긴 간선 출력 
def main():
    N = int(input())
    G = [[] for i in range(N)] # 간선간 연결 정보 저장
    for i in range(N-1):
        u, v, w = map(int, input().split())   # w = 가중치
        u -= 1  # 연결된 부모노드 
        v -= 1  # 자식노드 
        G[u].append((v, w))
        G[v].append((u, w))
    # 더 작은 가중치가 입력되면 갱신
    def dfs(a, p):
        # a --w--> b
        d = 0
        fs = []
        for b, w in G[a]:  # G[a] , a 와 연결된 모든 간선 + 가중치에 대해서 작업
            if b == p: # 현재 vertex가 목표 
                continue
            db, fb = dfs(b, a)
            d = max(d, db)
            fs.append(w + fb)

        fs.sort(reverse=True)
        d = max(d, sum(fs[:2]))
        f = 0 if len(fs) == 0 else fs[0]

        return (d, f)

    print(dfs(0, None)[0])


if __name__ == '__main__':
    main()