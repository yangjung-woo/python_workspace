# 1983. 조교의 성적 매기기 D2

# 학점은 상대평가로 주어지는데, 총 10개의 평점이 있다
# 총점 : 35 / 45 / 20

T = int(input())

for tc in range(1,1+T):
    N , K = map(int,input().split())
    score_list = []
    #  N 명 비율대로  0:  N : N /10
    div = N // 10
    Rank_list = ['A+', 'A0', 'A-', 'B+','B0','B-','C+', 'C0','C-','D0']
    for i in range(N):
        A,B,C = map(int,input().split())
        score = A * 0.35 + B *0.45 + C *0.2
        score_list.append(score)
    k_score = score_list[K-1]
    score_list.sort(reverse=True)

    rank = score_list.index(k_score)
    answer= Rank_list[rank // div]


    print(f'#{tc} {answer}')