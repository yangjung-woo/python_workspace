# 1974. 스도쿠 검증 D2
#입력으로 9 X 9 크기의 스도쿠 퍼즐
#겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 
#그렇지 않을 경우 0 을 출력한다.

def checks(arr):
    for i in range(9):
        # 숫자에 해당하는 idx에 1 추가
        # 요소에 숫자가 2이상인 것이 있으면 스도쿠 X
        # 가로 검사
        lst_h = [0] * 10
        # 세로 검사
        lst_v = [0]*10
        for j in range(9):
            # 가로검사
            lst_h[arr[i][j]] += 1
            if lst_h[arr[i][j]] == 2:
                return False
            # 세로 검사
            lst_v[arr[j][i]] += 1
            if lst_v[arr[j][i]] == 2:
                return False

    # 3*3 검사
    # x,y 3*3스도쿠 검사의 시작점
    for x in range(0,9,3):
        for y in range(0,9,3):
            # 3*3 검사
            lst_3 = [0] * 10
            for i in range(3):
                for j in range(3):
                    lst_3[arr[x+i][y+j]] += 1
                    if lst_3[arr[x+i][y+j]] == 2:
                        return False
    return True


T = int(input())
for tc in range(1,1+T):
    answer = 0
    sudoku = [[0]*9 for _ in range(9)]
    for i in range(9):
        sudoku[i] = list(map(int,input().split()))
    if checks(sudoku):  
        answer = 1
    else:
        answer = 0


    print(f'#{tc} {answer}')