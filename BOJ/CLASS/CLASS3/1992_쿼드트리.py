n = int(input())

board = []
for _ in range(n):

    board.append(list(map(int, list(input()))))


def filledWithZero(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 0:
                return False
    return True


def filledWithOne(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 1:
                return False
    return True


def splitBoard(board):
    one = []
    two = []
    thr = []
    fou = []
    for i in range(len(board)//2):
        one.append(board[i][:len(board)//2])
        two.append(board[i][len(board)//2:])
    for i in range(len(board)//2, len(board)):
        thr.append(board[i][:len(board)//2])
        fou.append(board[i][len(board)//2:])
    return one, two, thr, fou


def quadTree(board):
    answer = ''
    if filledWithOne(board):
        answer += '1'
    elif filledWithZero(board):
        answer += '0'
    else:
        answer += '('
        one, two, thr, fou = splitBoard(board)
        # print(one, two, thr, fou)
        answer += quadTree(one)
        answer += quadTree(two)
        answer += quadTree(thr)
        answer += quadTree(fou)
        answer += ')'
    return answer


print(quadTree(board))
