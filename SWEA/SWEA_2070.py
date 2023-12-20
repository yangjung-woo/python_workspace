# 2070. 큰 놈, 작은 놈, 같은 놈 D1

# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라

T = int(input())

for tc in range(1,1+T):
    A , B = map(int , input().split())

    if A < B:
        answer = '<'
    if A > B:
        answer ='>'
    if A == B:
        answer = '='
    print(f'#{tc} {answer}')