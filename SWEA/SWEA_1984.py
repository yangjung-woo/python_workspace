# 1984. 중간 평균값 구하기 D2
# 10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램을 작성하라.

# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)


T = int(input())

for tc in range(1,1+T):

    arr = list(map(int,input().split()))
    # 최대 최소 제거 
    sort_arr = sorted(arr)
    sort_arr.pop(0)
    sort_arr.pop(-1)
    # 8개에서 평균값 구하기 
    print(sort_arr)
    
    answer = int(round (sum(sort_arr)/len(sort_arr), 0 ))

    print(f'#{tc} {answer}')