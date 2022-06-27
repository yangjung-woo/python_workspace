
T =int(input())
case = [list(map(int, input().split())) for _ in range(T)] # 0 <n , m<100
 # (a^2 +b^2 +m) / (a*b) == 정수 를 만족하는 a b      n 
pair=[]

for _ in range(T):
    n= case[_][0]
    isin=case[_][1]
    cnt =0
    for i in range(1,n):
        for j in range(i+1,n):
            if((i*i + j*j + isin)% (i*j) ==0):
                cnt+=1

    print(cnt)
