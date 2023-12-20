# 2007. 패턴 마디의 길이 D2  논란의 여지가 있는 문제  

# 패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.
for i in range(1, int(input())+1):
    strr  = input()
    ans = ""
    for l in strr:
        ans += l
        if ans[:len(ans)//2] == ans[len(ans)//2:]: #문자열을 하나씩 검사해서 덧붙일 때 절반이 같으면 패턴
            print(f'#{i} {len(ans)//2}'); break