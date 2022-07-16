import sys

import heapq



class PriorityQueue:
    def __init__(self):
        self.arr =[None]
    def __len__(self):
        return self.arr -1
    def min(self):
        return self.arr[1]
    def push(self,v):
        self.arr.append(v)
        idx =len(self.arr) -1
        while idx != 1:
            if self.arr[idx//2]<= self.arr[idx]: # 부모자식 관계 
                return
            else:
                self.arr[idx//2], self.arr[idx] = self.arr[idx], self.arr[idx//2]
                idx //=2
    def pop(self):
        self.arr[1], self.arr[-1] =self.arr[-1], self.arr[1]
        self.arr.pop()
        idx =1 # idx 와 자식관계가 깨져있을수 있음 
        while True:
            min_idx = idx
            if 2*idx< len(self.arr) and self.arr[2*idx]< self.arr[min_idx]: #left
                min_idx =2*idx
            if 2*idx+1< len(self.arr) and self.arr[2*idx+1]< self.arr[min_idx]: #right
                min_idx =2*idx+1
            if idx == min_idx:
                break

def main():
    arr =[1,2,3,4,5]
    arr2=[5,4,3,8,1]
    Q =PriorityQueue()  
    # 파이썬 힙 모듈
    heapq.heapify(arr) # arr를  최소 힙으로 생성 
    heapq.heapify(arr2, reverse =True) # arr를 최대힙으로 생성 
    #heap min is arr[0]
    heapq.heappop(arr)
    heapq.heappush(arr, 7) 


if __name__ == '__main__':
    main()
