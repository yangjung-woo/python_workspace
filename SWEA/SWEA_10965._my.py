# 제곱수 만들기 
# 어떤 자연수가 소인수들의 곱으로 표현가능하다면
# 소인수들의 지수곱이 짝수이면 보다 작은 제곱합으로 표현 가능하다 

#step1 소수 리스트를 제작

prime_list=[2]
for i in range(3, int(10000000 ** (0.5)),2):
    for p in prime_list:
        if i % p ==0:  # 소수가 아닌 경우
            break
    else:
        prime_list.append(i)
'''
prime = [2]
for i in range(3, int(10000000 ** (0.5)), 2):
    for p in prime:
        if not i % p: 
            break
    else:
        prime.append(i)
        '''
answer = []
#Step2  최소값 B를 구하가

T= int(input())
answer_list = []
for tc in range(1,1+T):
    A = int(input())
    B = 1
    # A가 이미 거듭제곱 꼴이면 B =1 이다
    if A**0.5 == int(A**0.5):
        B = 1
    else: # 거듭제곱 꼴이 아니면 소수 리스트들로 소인수 분해
        for p in prime_list:
            cnt = 0
            while A % p ==0: # 0으로 나누어 떨어지면 계속 약분
                A = A // p 
                cnt = cnt +1
            if cnt % 2 !=0: # 0으로 나누어 떨어지지 않음 
                B = B*p
            if A == 1 or p > A:
                break
        if A >1:
            B= B*A
    answer_list.append("#{} {}".format(tc, B))
for answer in answer_list:
    print(answer)


