
def Doc (a,b,c):
    if b ==1: return a % c  #재귀문 탈출 포인트 a^1 일때  a%c 반환

    temp=Doc(a,b//2,c)# 분할 #ex 2^10 => 2^5 * 2^5  2^11 => 2^5 * 2^5 *2 

    #case 짝수
    if b %2 ==0: return temp*temp %c 
    #case 홀수 
    else: return temp*temp*a%c 
a,b,c =map(int,input().split())
# 지수분할 방식  2^5 = 2^2 * 2^2 *2
# Doc 분할 정복 사용
print(Doc(a,b,c))
