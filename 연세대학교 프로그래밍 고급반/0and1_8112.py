from collections import deque
# N 의 배수이면서 0,1로 이루어진 가장 작은 자연수를 찾는 문제

def solve(N):
    if N == 1: # 1 일경우 1 return 
        return '1'
    # par, num = P[x]
    # (par) 뒤에 (num)을 붙이면 x가 됨
    P = [None]*N

    # 모든 수는 1로 시작
    P[1] = (None, None)
    Q = deque([1]) # Q =[1]

    while len(Q) != 0:
        x = Q.popleft()
        # 0하고 1을 차례대로 순회, 나머지만 저장
        for v in range(2): # v = 0 or 1
            u = (10*x+v) % N  
            if P[u] is None:
                P[u] = (x, v)
                Q.append(u)

    if P[0] is None:  # bark 는 존재하지 않는다 비둘기집 원리
        return 'BRAK'

    # 역추적
    cur = 0
    ans = []
    while cur != 1:
        par, num = P[cur]
        ans.append(str(num))
        cur = par

    ans.append('1')
    return ''.join(ans[::-1])


def main():
    for i in range(int(input())):
        print(solve(int(input())))


if __name__ == '__main__':
    main()