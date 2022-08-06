
from collections import deque
import sys

def main():
    N = int(input())
    results =0
    argument_A = 0
    argument_B = 0

    A_list = list(map(int,sys.stdin.readline().split()))

    B_list = list(map(int,sys.stdin.readline().split()))
    A_list.sort()
    A= deque(A_list)

    for _ in range(N):
        results += B_list.pop(B_list.index(max(B_list))) * A.popleft()
        

    print(results)






    


if __name__ == '__main__':
    main()
