# 소득 불균형 10505
# n명의 사람의 소득이 주어졌을 때 이 중 평균 이하의 소득을 가진 사람들의 수를 출력해야 한다.

T = int(input())

for tc in range(1,1+T):
    N = int(input())
    money_list = list(map(int, input().split()))
    
    list_mean = sum(money_list) / N
    answer = 0
    for a in money_list:
        if a <= list_mean:
            answer +=1


    print(f"#{tc} {answer}")