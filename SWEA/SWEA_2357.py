# 2357. [AtCoder Beginner Contest 073] A. September 9 
# D2
# u are given a two-digit integer N. 
#Answer the question: Is 9 contained in the decimal notation of N?

T = int(input())

for tc in range(1,1+T):
    N = list(map(int,input()))
    if 9 in N:
        answer = "Yes"
    else:
        answer ="No"
    print(f"#{tc} {answer}")