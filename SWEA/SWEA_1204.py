# 최빈수 구하기 딕셔너리를 사용한다면 훨씬 수월   key : value   =  95 : 1 
T= int(input())

for tc in range(1,1+T):
    temp = int(input())
    scores= list(map(int,input().split()))
    count_dic = {} # 딕셔너리 생성   
    for i in scores:
        if i in count_dic:
            count_dic[i] += 1
        else:
            count_dic[i] = 1
    #print(count_dic)
    # 딕셔너리 완성 
    max_point = 0 
    # key : point
    max_freq= 0 
    # value = freq
    for point , freq in count_dic.items():
        if max_freq < freq:
            max_freq = freq
            max_point = point
        elif max_freq == freq:
            if max_point< point:
                max_point = point

    print('#{} {}'.format(temp, max_point) )