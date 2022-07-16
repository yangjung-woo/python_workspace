import heapq
import sys
def main():
    N = int(sys.stdin.readline())
    heap =[]
    for i in range(N):
        insert = int(sys.stdin.readline())
        heapq.heappush(heap,insert)
    while(heap):
        print(heapq.heappop(heap))
   

if __name__ == '__main__':
    main()
