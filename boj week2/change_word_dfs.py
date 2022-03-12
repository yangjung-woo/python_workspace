
answer = 0
def solution(begin, target, words):
 
    dfs(begin, target, 0, words)
    return answer
 
def change(A, B):  #  단어변환이 가능한지 아닌지 ture/false 반환 
    for i in range(len(A)):
        if A[:i]+A[i+1:] == B[:i]+B[i+1:]: #  i번째 단어만 다르고 다 같을때  ?? A=B 일때 동작오류? -> 이 함수 호출전에 G를동작
            return True
    return False
 
def dfs(begin, target, count, words):
    global answer
 
    if begin == target: # 정답 확인  확인  G  
        answer = count
        return
    else: # begin != target 
        if len(words) == 0: 
            return 
        for w in range(len(words)):
            if change(begin, words[w]): # word[w =0,1,2...] 변환 가능한 경우에만 동작 
                word = words[:w]+words[w+1:]  # word[] 는 words[0,1,2,3...]중에서 words[w]만 빠짐 -> words[w]는 방문한거 단정 
                dfs(words[w], target, count+1, word) 