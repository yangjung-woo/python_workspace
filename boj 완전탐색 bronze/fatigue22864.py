a,b,c,m = map(int,input().split())
# a: 1시간당 피로도  b: 1시간당 처리 c: 1시간 휴식당 a-C ,m: 피로도 상한선 

fatigue =0
work=0
if a > m : print(0)
else:
    for i in range(1,25):
        if (fatigue +a <= m):  # 피로도 한계 내 
            fatigue+= a
            work += b
        else: # 피로도 한계 초과시 
            if (fatigue-c >=0):
                fatigue-=c
            else: # 피로도 음수 = 일안함 
                fatigue=0
    print(work)