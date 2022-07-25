import sys


def main():
    n = int(input())
    m = int(input())
    inf = 100000000

    Map = [[inf] * n for i in range(n)]  
    # map은 N개의 vertex 간의 최단 경로만 저장되어있다 
    for i in range(m):    # 입력값 a ,b ,c 에 대해서 가장 최단경로만 저장 하는 map
        a, b, c = map(int, input().split())
        if Map[a - 1][b - 1] > c:
            Map[a - 1][b - 1] = c
    # 모든 관계에 대해서  i -> j 로 이동 경로  중간에 거쳐 지나가는 정점 k 에 대해 
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j and Map[i][j] > Map[i][k] + Map[k][j]:   # 중간에 거쳐가는게 더 짧을시 map 갱신
                    Map[i][j] = Map[i][k] + Map[k][j]
    for i in Map:
        for j in i:
            if j == inf:
                print(0, end=' ')
            else:
                print(j, end=' ')
        print()



if __name__ == '__main__':
    main()
