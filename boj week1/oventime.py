
while (1):

 hour,minute = input("시간과 분을 입력해주세요: ").split() #공백으로 문자열 구분
# input은 문자열로 입력받기 때문에 정수로 변환 -> 조건문에 사용 가능
 hour=int(hour)
 minute=int(minute)
 if 0<=hour<=23 and 0<=minute<=59:break
 else:print("다시 입력해 주세요")

while(1) :
 cooking= input("몇분동안 하시겠습니까?")
# input은 문자열로 입력받기 때문에 정수로 변환을 해줘야 조건문에 사용 가능
 cooking=int(cooking)
 if 0<=cooking<=1000: break
 else:print("잘못된 값입니다 다시 입력해주세요")



cooking_hour= cooking//60 # (/)나누고 소숫점 까지 저장 (//) 나누고 정수만 저장 
cooking_minute= cooking%60 #나머지 

hour=hour +cooking_hour
minute=minute+cooking_minute

if minute>60:
     hour=hour+1
     minute=minute-60
     if hour>=24:
        hour=hour-24

print("완성 시간은 {h} 시 {m} 분 입니다 ".format(h=hour,m=minute))
        
    


        

    
