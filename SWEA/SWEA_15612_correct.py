t = int(input())
for test_case in range(t):
    board = []
    for i in range(8):
        board.append(list(map(str, input())))

    row = [0, 0, 0, 0, 0, 0, 0, 0]
    col = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(8):
        for j in range(8):
            if board[i][j] == 'O':
                row[i] += 1
                col[j] += 1

    answer = 'yes'
    for x in row:
        if x != 1:
            answer = 'no'

    for y in col:
        if y != 1:
            answer = 'no'

    print(f"#{test_case+1} {answer}")