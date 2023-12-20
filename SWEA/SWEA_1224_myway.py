type1 = {'(': 3, '*': 2, '+': 1, ')': 0}
type2 = {'(': 0, '*': 2, '+': 1}


def fix_post(arr):
    temp = []
    stack = []
    for i in arr:
        if i in type1.keys():
            if not stack: # stack 이 비어있다면 연산자 stack 에 그대로 in 하지만 거의 이런 경우 없을
                stack.append(i)
            elif i ==')':
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
            else:
                while type1[i] <= type2[stack[-1]]:
                    temp.append(stack.pop())
                stack.append(i)
        else:
            temp.append(i)
    return temp
