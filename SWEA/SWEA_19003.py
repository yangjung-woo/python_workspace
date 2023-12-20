# 팬린드롬 문제 D3 


TC = int(input())
for tc in range(1,TC+1):
    Fanlin_flag = False # 팬린드롭수가 존재하면 True로 바뀜 
    N, M = map(int,input().split())
    N_fan_list =[]
    answer = 0
    nofan_add=0
    cnt = 0
    for i in range(N):
        input_str = input().rstrip()
        N_fan_list.append(input_str)
        if input_str[::] == input_str[::-1]: # 입력 문장이 팬린드롬이면 
            Fanlin_flag = True
            N_fan_list.pop()
        # no 팬린 드롭 리스트가 생성됨  

    for _ in range(len(N_fan_list)):
        temp = N_fan_list.pop()
        if temp[::-1] in N_fan_list: 
            nofan_add +=  2*M
    
    if Fanlin_flag:  # 순수 팬린드롬 문자열이 있을 경우
        answer = M + nofan_add
    else:
        answer = nofan_add
    
    print('#{} {}'.format(tc, answer))