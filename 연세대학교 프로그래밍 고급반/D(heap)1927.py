import heapq
import sys


def main():
    N = int(sys.stdin.readline())
    heap =[]
    heapq.heapify(heap)
    for i in range(N):
        command = int(sys.stdin.readline())
        if command ==0:
            if len(heap) ==0:
                print(0)
            else:
                print(heapq.heappop(heap))
        elif(command<0):
            continue
        elif(command>0):
            heapq.heappush(heap,command)
        



if __name__ == '__main__':
    main()





