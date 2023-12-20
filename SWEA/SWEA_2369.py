# B. Theater
#Joisino is working as a receptionist at a theater.

# The theater has 100000 seats, numbered from 1 to 100000.
# N groups of audiences have come so far
#  i-th group occupies the consecutive seats from Seat Li to Seat Ri (inclusive).
# D2
# How many people are sitting at the theater now?

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    answer = 0
    for i in range(N):
        Li , Ri =  map(int, input().split())  # Li ~ Ri 까지 자리를 차지함 
        answer += abs(Li -Ri)+1

    print(f'#{tc} {answer}')