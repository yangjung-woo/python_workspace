
import sys
stack= []
n =int(input())
print_list =[]
for i in range(n):

    command_list = sys.stdin.readline().split()

    if (command_list[0] =="push"):
        stack.append(command_list[1])
    elif(command_list[0] =="pop"):
        if len(stack)<=0:
            print_list.append(-1)
        else: print_list.append(stack.pop())
    elif(command_list[0] =="size"):
        print_list.append(len(stack))
    elif(command_list[0] =="empty"):
        if len(stack)<=0:
            print_list.append(1)
        else: print_list.append(0)
    elif(command_list[0] =="top"):
        if len(stack)<=0:
            print_list.append(-1)
        else: print_list.append(stack[-1])

for i in print_list:
    print(i)