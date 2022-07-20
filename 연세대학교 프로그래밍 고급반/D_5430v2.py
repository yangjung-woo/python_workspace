from collections import deque
from ntpath import join
import queue
import sys

def main():
    T = int(sys.stdin.readline())

    for _ in range(T):
        commands = sys.stdin.readline().rstrip()
        N =  int(sys.stdin.readline())
        arr = sys.stdin.readline().rstrip()[1:-1].split(',')  # [1:-1] 1 부터 N-1까지("[]"생략)
        queue = deque(arr)
        if N==0:
            queue = []
        
        flag=do_work(commands, N, queue)
        if flag:
            print('['+','.join(queue)+']')
        else: print("error")


def do_work(commands, lenth , queue): 
    reverse_flag =False

    for k in range(len(commands)):
        if commands[k]=='R':
            if reverse_flag:
                reverse_flag=False
            else:
                reverse_flag=True

        elif commands[k]=='D':
            if len(queue)==0:y
                return False
            else:
                if reverse_flag==False:
                    queue.popleft()
                else:
                    queue.pop()
    
    if reverse_flag ==True:
        queue.reverse()
    return True

if __name__ == '__main__':
    main()
