# n-queen 문제 점유하는 놓을수 없으면 1 , 놓을수 있으면 1

def check(arr, cnt) :
    global n, result
    if cnt == n :
        result += 1
        return
    temp = [0] * n
    for i in range(len(arr)) :
        # 열
        temp[arr[i]] = 1
        # 왼쪽 대각선
        if arr[i] - (cnt - i) >= 0 : # 범위 내에 있다면
            temp[arr[i] - (cnt-i)] = 1
        # 오른쪽 대각선
        if arr[i] + (cnt - i) < n : # 범위 내에 있다면
            temp[arr[i] + (cnt-i)] = 1

    for i in range(n) :
        if temp[i] == 0 : # 빈 칸이라면
            check(arr + [i], cnt + 1)

t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    result = 0
    check([], 0)

    print('#%d %d' % (tc, result))