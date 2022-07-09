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

        if (flag==False):
            print("error")
        else:
            print('['+','.join(queue)+']')

def do_work(commands, lenth , queue): 
    one_more_jump =False
    for k in range(len(commands)):

        if one_more_jump==True:
            one_more_jump=False
            continue
        else:
            if commands[k] =='R' and commands[k+1]=='R': # R 2번 연속시 동작 x
             one_more_jump =True
             continue

            else:

                if commands[k] == 'R': #뒤집기
                    queue.reverse()

                elif commands[k] == 'D': # 버리기 
                    if len(queue) >0:
                        queue.popleft()
                    else:
                        return False
    return True

if __name__ == '__main__':
    main()
