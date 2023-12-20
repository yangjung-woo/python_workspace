# 완전 탐색 문제 (모든 케이스 구하고 그중 최소값 )  최대 상금 문제
# set 을 응용한 방법    set 자료구조 : 중복을 허용하지 않음 , 순서가 없음 
T = int(input())

for tc in range(1,1+T):
    a , chance = input().split()
    chance = int(chance)
    now = set([a])
    nxt =set()  # set은 중복을 허용하지 않는다 
    for c in range(chance):
        while now:
            s= now.pop()
            s= list(s) #  now = '123'    => s = ['1' , '2' , '3']

            for i in range(len(a)-1):
                for j in range(i+1,len(a)):
                    s[i], s[j] = s[j], s[i]
                    nxt.add(''.join(s))# 교환 가능한 모든 경우를 nxt에 넣음 
                    s[i], s[j] = s[j], s[i] # 원상복구
        now ,nxt = nxt, now
    
    answer = max(map(int, now)) # 최대 상금은 여기에 저장 
    print('#{} {}'.format(tc,answer)) 
