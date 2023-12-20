# 가능한 시험점수 
# 영준은 N 개 문제를 만듦
# 문제마다 배점이 다르고 틀리면 0점 
# 학생이 받을수 있는 점수의 경우의 수  DFS 문제 하지만 시간초과
# 따라서 이 문재는 DP 를 사용  

print("program is start \n")
T = int(input())
for t in range(1,T+1):
    N = int(input())
    score = list(map(int,input().split()))
    score_visit = [1] + [0] * sum(score) # 0 점은 반드시 존재
    score2 = [0] # 모든 가능한 점수 리스트 
    for point in score: # 점수를 뽑아서 
        for i in range(len(score2)): # 결과와 더해 나간다.
            if not score_visit[point+score2[i]]: # 더한 값이 방문한적 없으면 중복이 아니기에 
                score_visit[point+score2[i]] = 1 # 방문 배열에 체크하고
                score2.append(point+score2[i]) # 결과에 더해준다
    print('#{} {}'.format(t,len(score2)))