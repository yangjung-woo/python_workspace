# 17319. 문자열문자열 D3
#  문자열 하나를 받아 그대로 두 번 연달아 썼다. 
#예를 들어 “abc” 를 받았다면 “abcabc” 를 썼다.

T = int(input())

for tc in range(1,1+T):

    N = int(input())
    s = list(input())
    if s[0:N//2:] == s[N//2::]:
        answer = "Yes"
    else:
        answer = "No"
    print(f'#{tc} {answer}')