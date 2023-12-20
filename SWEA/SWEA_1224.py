# 계산식을 후위 표기법으로 변동하여 계산하는 프로그램
# 1.주어진 숫자는 그대로 append 하되  문자  * + ( ) 에 대한 조건을 작성
# 2. 조건을 스택을 사용하여 우선순위 반영

# 후위 표기법으로 변경
icp = {'(': 3, '*': 2, '+': 1, ')': 0}
isp = {'(': 0, '*': 2, '+': 1}

def postfix(a):
    stack = []
    temp = []
    for e in a:
        if e in icp.keys():
            if not stack:
                stack.append(e)
            elif e == ')':
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
            else:
                while icp[e] <= isp[stack[-1]]:
                    temp.append(stack.pop())
                stack.append(e)
        else:
            temp.append(e)
    while stack:
        temp.append(stack.pop())
    return temp

def calculate(a):
    stack = []
    for e in a:
        if e == '+':
            stack.append(stack.pop() + stack.pop())
        elif e == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(e))
    return stack[0]


for tc in range(1, 11):
    n = int(input())
    print('#{0} {1}'.format(tc, calculate(postfix(input()))))