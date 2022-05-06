N=int(input())
L=[]
for i in range(N): # list L 에 word 입력
    word=input()
    L.append(word)

L.sort(key=len) # 길이 순으로 정렬 가장 짧은 단어가 맨앞으로 
ans=0
for i in range(N):
    nowWord=L[i]
    isHead=False
    for j in range(i+1,N):
        try:
            if L[j].index(nowWord)==0:
                isHead=True
                break
        except:
            continue
    if not isHead:
        #print(nowWord)
        ans+=1
print(ans)