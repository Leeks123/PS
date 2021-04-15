def rotateBoard(board):
    ret = [[0]*len(board) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            ret[j][i] = board[i][j]
    return ret


def solve():
    n = int(input())
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))
    board = rotateBoard(board)

    flag = 0
    cnt = 0
    for i in range(n):
        for j in range(n):
            if flag == 0:
                if board[i][j] == 1:
                    flag = 1
            elif flag == 1:
                if board[i][j] == 2:
                    flag = 2
                    cnt += 1
            elif flag == 2:
                if board[i][j] == 1:
                    flag = 1
        flag = 0

    return cnt


for i in range(1, 11):
    answer = solve()
    print('#'+str(i), answer)
