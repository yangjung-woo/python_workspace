from binascii import a2b_hex
from re import A
import sys


N =int(input())
x = 0
temp_list=[]
qury_list=[]
minus_cnt =0
for i in range(6):
    temp_list = list(map(int ,sys.stdin.readline().split()))
    if len(qury_list)<=0 :
        if temp_list[0] ==1:
          a= temp_list[1]
          b= temp_list[2]
          qury_list.append([a,b])

        elif temp_list[0] ==2:
            
            total =1
            if temp_list[1]*a + b <0:
                print('-')
            elif temp_list[1]*a + b >0:
                print('+') 
            elif temp_list[1]*a + b ==0:
                print('0')
    else:
        if temp_list[0] ==1:
          a= temp_list[1]
          b= temp_list[2]
          qury_list.append([a,b])

        elif temp_list[0] ==2:
            total =1

            for j in range(len(qury_list)):
                total =  (temp_list[1]* qury_list[j][0] +qury_list[j][1]) *total

                
                if total ==0: # 0이면 바로 0xN =0 이므로 탈출
                    print('0')
                    break

            if total<0:
                print('-')
            elif total >0:
                print('+') 
            


