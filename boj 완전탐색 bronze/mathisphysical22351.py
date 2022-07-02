import sys
string =sys.stdin.readline()
#1 처음 부터 오름차순으로 정렬한 문자열 생성
#2 문자열이 1 10 100 인경우의수 분기점 생성
def sotring(start,length):
    c_set =''
    first = str(start)
    end=''
    for i in range(start,1000):
        if len(c_set)>= length: # 탈출지점 최대길이 돌파
            break
        c_set += str(i) # c_set 에 start~1000까지 숫자 저장
        end =str(i) # end 는 갱신 
    return c_set,first,end
def case_of_arr ():
    cases=[]
    cases.append(sotring(int(string[0]), len(string)))
    if len(sotring) >= 2:
        cases.append(sotring(int(sotring[0:2]), len(sotring))) #10~99
    if len(sotring) >= 3:
        cases.append(sotring(int(sotring[0:3]), len(sotring))) #100~999
    if len(sotring) >= 4:
        cases.append(sotring(int(sotring[0:4]), len(sotring))) #1000~2889
    for i in range(3):
     if sotring == cases[i][0]:
        print(cases[i][1], cases[i][2])
        break
case_of_arr()