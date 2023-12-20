#1986. 지그재그 숫자 D2

# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자
def sum_of_zigzag(N):
    a=[-1,1] # 0 짝수면 -1 , 홀수면 +1 
    total = 0
    for i in range(1,1+N):
        total += a[i%2] * i
    return total

T = int(input())

for tc in range(1,1+T):
    N = int(input())
    answer = sum_of_zigzag(N)
    print(f'#{tc} {answer}')