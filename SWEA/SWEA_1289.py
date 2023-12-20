# 원재의 메모리 복구하기 
# 예를 들어 지금 메모리 값이 0100이고, 3번째 bit를 골라 1로 설정하면 0111이 된다.
#원래 상태가 주어질 때 초기화 상태 (모든 bit가 0) 에서 원래 상태로 돌아가는데 최소 몇 번이나 고쳐야 하는지 계산해보자.

T = int(input())

for tc in range(1,1+T):

    arr = list(map(int,input()))
    flag = 0
    answer = 0
    for a in arr:
        if a != flag:
            flag = a 
            answer +=1 
    print(f"#{tc} {answer}")