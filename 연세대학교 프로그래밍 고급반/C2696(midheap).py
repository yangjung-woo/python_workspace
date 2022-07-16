import heapq
import sys
def find_mid(heap_data):
    left_heap=[] # 최대 힙   mid 보다 작은 집합 이중 가장 큰값이 필요하므로 최대힙
    right_heap=[] # 최소 힙  mid 보다 큰 집합 이중 가장 작은값이 필요하므로 최소힙 
    middle =heap_data[0]
    result=[middle]
    for i , value in enumerate(heap_data[1:],start=1):
        if value > middle:
            heapq.heappush(right_heap,value)
        else:
            heapq.heappush(left_heap,(-value,value))
        if i %2 ==0: # 짝수 번째 
            if len(left_heap)<len(right_heap): # left heap 이 더 짧으면 middle ->leftheap , 

                heapq.heappush(left_heap,(-middle,middle))
                # right heap[0](root) -> middle
                middle=heapq.heappop(right_heap)

            elif len(left_heap)>len(right_heap):
                heapq.heappush(right_heap,middle)
                middle=heapq.heappop(left_heap)[1]
            result.append(middle)
    print(len(result))
    for i in range(len(result)):
        if i!= 0 and (i+1)%10 ==1:
            print() # 줄바꿈
        print(result[i],end=' ')
    print()
        



def main():
    
    T = int(sys.stdin.readline())
    for i in range(T):
        heap =[]
        N = int(sys.stdin.readline())
        if N %10 ==0:
            for _ in range(N//10): #10개씩 입력
                heap.extend(list(map(int,sys.stdin.readline().split())))
        else:
            for _ in range(N//10 +1): # 10개 +a 입력
                heap.extend(list(map(int,sys.stdin.readline().split())))
        find_mid(heap)

if __name__ == '__main__':
    main()
