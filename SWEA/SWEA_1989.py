# 1989. 초심자의 회문 검사 D2

T = int(input())


for tc in range(1,1+T):

    arr = input()
    if arr[::] == arr[::-1]:
        answer = 1
    else:
        answer = 0
    print(f'#{tc} {answer}')