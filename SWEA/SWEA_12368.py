#D3 24시간 


T = int(input())
for i in range(1,T+1):
    currnet , hour = map(int,input().split())

    print('#{} {}'.format(i,(currnet+hour)%24))