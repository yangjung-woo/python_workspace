import heapq
import sys


def main():
    n,k = map(int,input().split())
    lis_jewel = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    lis_bag =[int(sys.stdin.readline()) for _ in range(k)]

    lis_bag.sort()
    lis_jewel.sort()
    tmp =[]
    result =0
    for bag in lis_bag:
        while lis_jewel  and bag >=lis_jewel[0][0]: # max 힙 생성
            heapq.heappush(tmp, -lis_jewel[0][1])
            heapq.heappop(lis_jewel)
        if tmp :
            result += heapq.heappop(tmp)
        elif not lis_jewel :
            break
    print(-result)
        

        





    


if __name__ == '__main__':
    main()
