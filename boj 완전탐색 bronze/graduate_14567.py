from collections import deque
import sys


def main():
    N,M =map(int,sys.stdin.readline().split())
    in_degree =[0 for _ in range(N+1)]
    when_cur = [0 for _ in range(N+1)]
    G=[[] for _ in range(N+1)]
    q=deque()
    for _ in range(M):
        a,b = map(int,sys.stdin.readline().split())
        in_degree[b] +=1
        G[a].append(b)

    # 위상정렬 시작 
    for i in range(1,N+1):
        if in_degree[i]==0: # 진입차수가 0이면 
            q.append((i,1)) # 진입 차수가 0인 정점을 queue 에 삽입
            when_cur[i]= 1 # 진입 차수가 0인 과목 -> 1학기때 이수 가능
    while q:
        target, now_cur = q.popleft()
        for i in G[target]:
            in_degree[i] -=1
            if in_degree[i]==0:
                q.append((i,now_cur+1))
                when_cur[i] = now_cur +1
    print(*when_cur[1:])

    


if __name__ == '__main__':
    main()