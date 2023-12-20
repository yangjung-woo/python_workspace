# 간단한 369 게임 
n= int(input())
for i in range(1,1+n):
    str_i= str(i)
    clap_cnt = str_i.count("3")+str_i.count("6")+str_i.count("9")

    if clap_cnt == 0:
        print(i,end=' ') # print 의 default end = \n
    else:
        print('-'*clap_cnt,end =' ')