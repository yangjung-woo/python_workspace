from collections import defaultdict
def nextWord(cur, words):
    ret = [] # cur에서 방문가능한 노드들을 저장 
    for word in words: # words[hot,hog,dog...]을 하나씩 cur 과 비교
        cnt = 0
        for idx in range(len(word)):
            if word[idx] == cur[idx]:  
                cnt += 1
        if cnt == len(cur)-1: # 단어가 1개만 다르다 == 이동할수 있는 노드다!
            ret.append(word) # ret 에 저장 
    return ret
def bfs(begin, target, words):
    visited = defaultdict(lambda: False)
    queue = nextWord(begin, words) ## begin 에서 방문 가능한 노드들이 큐에저장
    count = 0
    min = 1e9 # 최대한 작은 최솟값 설정 
    while(len(queue) > 0): # begin 에서 갈수있다!면 탐색
        size = len(queue)
        count += 1 # 탐색 할때마다 count 1증가 
        for _ in range(size): #queue의 size = begin 에서 방문가능한 노드들 수 만큼 반복
            key = queue.pop(0)  # queue 에서 꺼냄
            visited[key] = True # 거기로 방문 
            if (key == target and count < min):# 찾았다!  그럼 찾을때 까지 걸린 count 저장
                # 만약 더 작은 count가 있다면 min 갱신 
                min = count 

            for candidate in nextWord(key, words):  # 처음 nextWord(begin word) -> nextWord(key,words)
                if (visited[candidate] == False): #방문 아직 안했다? queue(추후 방문예정)에 추가
                    queue.append(candidate)
    if min == 1e9:
        return 0
    else:
        return min

def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer