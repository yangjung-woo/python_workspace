from pickletools import string1
from random import * #random 선언 

#   quiz 
print (randint(4,28)) #1~46중 하나 출력
studyday =randint(4,28)
print("오프라인 스터디 모임 날자는 매월"+str(studyday)+"일로 정해졌습니다")
#문자열 출력
sentence="아이엠 그루트"
print(sentence)
sentence3="""
하이 에브리원
예아 
스터딩
"""
print(sentence3)

#슬라이싱 문자열을 끊어서 원하는 자료를 출력 
jumin ="990105-1032512"
print("sex:"+jumin[7]) 
print("year:"+jumin[0:2]) #99
print("month:"+jumin[2:4]) #01
print("day:"+jumin[4:6]) #01

print("front jumin:"+jumin[:6]) #990105 처음부터 6번째 직전까지
print("back jumin:"+jumin[7:]) #7번째부터 끝까지 1032512
print("back jumin:"+jumin[-7:]) #뒤에서 7번째부터 끝까지

#문자열 처리함수 
string1 ="Power make groly"
print(string1.lower()) #string을 소문자 화
print(string1.upper()) #대문자
print(string1[0].islower()) # 소문자면 true 아님 false
print(len(string1)) #문자열 길이 출력
print(string1.replace("make", "supper")) #make를 찾아 있으면 supper로 변환

index = string1.index("P") #index에 n이 위치하는 번호를 전가
print(index) # 못찾으면 error 출력

print(string1.find("java"))# 문자열에서 문자 찾기 만약 못찾으면 -1
print(string1.count("r"))#문자열에서 r 갯수 

#문자열 포멧 
print("나는 %d 살 입니다 " %45)
print("나는 %s 살 입니다 " % "삼겹")
print("나는 학점 %c 입니다 " % "A")

print("나는 {} 살 입니다 " .format(20))
print("나는 {}살 이고 취미는 {} 입니다".format(20,"운동"))
print("나는 {age}살 이고 취미는 {hobby} 입니다".format(hobby="운동",age=20))

age1= 20
hobby1="운동"
print(f"나는 {age}살 이고 취미는 {hobby} 입니다".format(hobby="운동",age=20))

#탈출문자 1:10:01

