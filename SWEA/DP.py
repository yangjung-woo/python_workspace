# 다이나믹 프로그래밍 

dp_list =[0]*100 # Dp는 모든 과정 단계를 배 열 혹은 리스트에 넣는다 
def fibo(x): # 재귀 호출의 피보나치의 문제점   n = 50만 되어도 중복되는 계산랑이 많아져서 오래걸림 
    global dp_list
    if (x==1): return 1

    if (x==2): return 1
    if (dp_list[x]!=0):
        return dp_list[x]
    dp_list[x] = fibo(x-1) + fibo(x-2)
    return dp_list[x]



print(fibo(70))#  d
