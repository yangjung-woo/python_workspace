import sys

N =int(input())
temp_list=[]
qury_list=[]
minus_cnt =0
for i in range(N):

    temp_list = list(map(int ,sys.stdin.readline().split()))  # 명령어 라인 입력
    if len(qury_list)<=0: # 최초 시행
        if temp_list[0] ==1:
          a= temp_list[1]
          b= temp_list[2]
          qury_list.append([a,b])

        elif temp_list[0] ==2:
            
            if temp_list[1]*a + b <0:
                print('-')
            elif temp_list[1]*a + b >0:
                print('+') 
            elif temp_list[1]*a + b ==0:
                print('0')
    else:  # 2~N  번 시행 동작
        if temp_list[0] ==1:
          a= temp_list[1]
          b= temp_list[2]
          qury_list.append([a,b])

        elif temp_list[0] ==2:
            total =1

            for j in qury_list:
                total =  temp_list[1]* j[0] +j[1]  # 모든 f(x)  (a1)x+b1  , (a2)x+b2....(an)x+b   = total 
                if total ==0: # 0이면 바로 0xN =0 이므로 탈출
                    print('0')
                    minus_cnt=0
                    break
                elif total <0:
                    minus_cnt+=1
            if (minus_cnt !=0):
                if minus_cnt%2==0: #  음수가 (2개) 짝수개 발생 시  +
                    print('+')
                elif minus_cnt%2==1: # - 홀수개 => 음수
                    print('-')    
            


