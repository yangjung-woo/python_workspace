prime = [2]
for i in range(3, int(10000000 ** (0.5)), 2):
    for p in prime:
        if not i % p: 
            break
    else:
        prime.append(i) # 소수들을 담은 리스트를 생성 
answer = []
T = int(input())
for tc in range(1,T+1):
    A = int(input())
    res = 1
    if A**0.5 != int(A**0.5): # A 가 제곱근이 아닌 경우 소수 리스트들 사이에서 곱했을때
        # 제곱근이 되는 수가 있는지 확인 
        for p in prime:
            cnt = 0
            while not A % p: # A 를 소수로 나누었을때 0이면 cnt +1 약수 수 증가
                A //= p
                cnt += 1
            if cnt % 2: # 지수가 짝수 제곱으로 표현 가능하다 
                # 하지만 지수가 홀수 면 표현할 수 없기때문에 짝수로 맟춰줘야 한다 
                res *= p
            if A == 1 or p > A:
                break
        if A > 1:
            res *= A
    answer.append('#{} {}'.format(tc, res)) # 메 단계 print 는 매우 많은 시간을 잡아 먹는다
    # 따라서 출력할 문장들을 리스트에 저장하고 출력하는 것도 좋은 방법
for ans in answer:
    print(ans)