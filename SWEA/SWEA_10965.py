# 제곱수 만들기 
# 어떤자연수 A 가 주어짐 , 여기에 B 를 곱했을때 거듭제곱수가 되는 
# 최소의 B 를 구하는 프로그램을 작성해라 

def check_(int_a):
    if int_a**0.5 == int(int_a**0.5):
        return True
    else:
        return False
    
T= int(input())

for tc in range(1,1+T):

    A = int(input())
    B = A 
    for i in range(1,int(A**0.5)+1):
        if i < B and check_(i*A) :
            B = i
            break

    answer = B
    print("#{} {}".format(tc, answer))