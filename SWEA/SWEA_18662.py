#18662. 등차수열 만들기
#세 정수 a,b,c가 주어진다. 
#당신은 음이 아닌 실수 x을 정한 뒤, 세 정수 중 하나에서 x만큼을 더하거나 뺄 수 있다. 
#당신은 이러한 작업을 정확히 한 번 하여 a,b,c가 등차수열을 이루도록 하려고 한다. 

T = int(input())

for tc in range(1,1+T):

    a , b ,c = map(int,input().split())
    L_diff= b-a
    R_diff = c-b
    if L_diff == R_diff:
        answer = 0.0
    else:
        answer = abs(R_diff - L_diff)/ 2   # |a+c -2b| / 2 = answer

    print(f"#{tc} {answer}")