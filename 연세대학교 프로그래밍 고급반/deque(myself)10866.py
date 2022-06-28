from collections import deque
import sys

from numpy import append
n = int(input())
dq =deque()
print_list=[]

for i in range(n):
    command_list = sys.stdin.readline().split()  # command [0] = 명령어  command [1] = 값
    if command_list[0] == "push_front": #
        dq.appendleft(command_list[1])
    elif command_list =="push_back":
        dq.append(command_list[1])

    elif command_list[0] =="pop_back": #  출력
        if dq:
            print_list.append(dq[len(dq)-1])
            dq.pop
        else: print_list.append(-1)

    elif command_list[0] =="pop_front": # 출력
        if dq:
            print_list.append(dq[0])
            dq.popleft()
        else:print_list.append(-1)

    elif command_list[0] =="size": #출력
        #print(len(dq))
        print_list.append(len(dq))
    elif command_list[0] =="empty":  # 0 or 1 출력
        if dq:
            print_list.append(0)
        else: print_list.append(1)

    elif command_list[0] =="front": #가장앞 출력
        if dq:
            print_list.append(dq[0])
        else:print_list.append(-1)
    elif command_list[0] =="back": # 가장 뒤 출력
        if dq:print_list.append(dq[len(dq)-1])
        else:print_list.append(-1)  #deque(-1) = 뒤에서 첫번째

for j in print_list:
    print(j)