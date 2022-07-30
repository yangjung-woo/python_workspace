import sys
sys.setrecursionlimit(10**9) #pypy3에서는 정확한 크기를 할당하는 것이 아니라 대략적으로 크기를 할당하기 때문에 위와 같은 문제가 발생하게 됩니다.
#출처: https://imksh.com/46 [강승현입니다:티스토리]

N ,R , Q = map(int,sys.stdin.readline().split())
G = [[] for _ in range(N+1)] # 간선간 연결 정보 저장
count = [0]*(N+1)

def counting_vertex(Root):
        count[Root]=1
        for i in G[Root]:
            if not count[i]:
                counting_vertex(i)
                count[Root]+=count[i]


def main():

    for i in range(N-1):
        u,v=map(int,sys.stdin.readline().split())
        G[u].append(v)
        G[v].append(u)

    counting_vertex(R)

    for i in range(Q):
        qury= int(sys.stdin.readline())
        print(count[qury])


if __name__ == '__main__':
    main()
