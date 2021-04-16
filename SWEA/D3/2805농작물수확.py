t = int(input())


def solve(board, n):
    ret = 0
    for i in range(n//2+1):
        ret += sum(board[i][n//2-i:n//2+i+1])
    for i in range(n//2+1, n):
        ret += sum(board[i][i-n//2:n+n//2-i])
    return ret


for i in range(1, t+1):
    n = int(input())

    board = []
    for _ in range(n):
        board.append(list(map(int, list(input()))))

    answer = solve(board, n)
    print('#'+str(i), answer)
