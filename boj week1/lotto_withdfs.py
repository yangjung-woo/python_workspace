def dfs(start, depth): 
    if depth == 6: ## 입력한 번호수 6 개 조합 출력
        for i in range(6):
            print(combi[i], end=' ')
        print()
        return
    for i in range(start, len(s)): ## 7개 이상일 경우 재귀 호출 
        combi[depth] = s[i] #combi 는 로또 조합 
        dfs(i + 1, depth + 1) ## 다시 재귀움 

combi = [0 for i in range(13)] #6<k<13 

while True:
    s = list(map(int, input().split())) # 번호 줄을 s에 입력 띄어쓰기로 구분 
    if s[0] == 0:
        break
    del s[0] #첫 문자열 제거? 첫 숫자는 N개의 조합을 뜻함 그후 x1...xn 개
    dfs(0, 0)
    print() # 1