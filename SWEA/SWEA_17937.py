#17937. 큰 수의 최대공약수

def gcd_recursive(a,b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)
    
def gcd_iterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a

T = int(input())

for tc in range(1,1+T):
    A , B = map(int, input().split())
    C = gcd_iterative(A,B) #가장 큰 값 B와 가장작은 A의
    # 큰 최대 공약수를 찾음 
    # A~B 사이의 최대공약수를 찾기 
    for i in range(A ,B+1):
        C = gcd_iterative(C,i)
        if C == 1: # 만약 A 가 1부터 시작이면 최대 공약수는 반드시 1뿐임을 추가 
            break

    print(f'#{tc} {C}')