# 2056. 연월일 달력 D1

T = int(input())
dic = {"01":31 ,"02":28, "03": 31, "04":30,
       "05":31 , "06":30 , "07": 31 , "08" :31 , 
        "09":30 , "10": 31 , "11":30 , "12":31 }

for tc in range(1,T+1):
    
    YYMMDD = input()
    # 0 1 2 3    /  4 5  / 6 7 
    MM = YYMMDD[4:6:]
    DD =int((YYMMDD[6::]))
    if MM not in dic:
        answer = '-1'
    else:
        KK = dic[MM]
        if DD <= KK:
            answer =  YYMMDD[0:4:] + '/'+ YYMMDD[4:6:] +'/' +YYMMDD[6::]
        else:
            answer = "-1"
    print(f"#{tc} {answer}")