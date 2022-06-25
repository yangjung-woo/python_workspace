import sys
n = int(sys.stdin.readline()) #  n = int(input())
words = [(sys.stdin.readline()).rstrip() for _ in range(n)]
Xlist=[] # 정답 저장용 X 리스트
#strip() 문자열에서 argument 문자를 제거 argument 없을시 공백 제거  lstript ,rstript

words.sort(key=len)
res = 0

# 반복문을 통해 단어를 확인
for i in range(n):
    flag = False
    # 현재 단어보다 길이가 긴 단어를 확인
    for j in range(i + 1, n):
        # 현재 단어가 접두사인지 확인
        if words[i] == words[j][0:len(words[i])]:#  (h  ,haa) 비교시 words[i] ==h, word[i+1]= haa 
            flag = True 
            break
    
    # 현재 단어가 접두사가 아니라면 res 카운트
    if not flag:
        Xlist.append(words[i])
        #print(Xlist) 리스트 확인용 

print(len(Xlist))