
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, list(input()))))


def dfs(v):
    global board
    if board[v[0]][v[1]] != 0:
        return False
    else:
        board[v[0]][v[1]] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = v[1]+dx[i]
        ny = v[0]+dy[i]
        if nx >= 0 and nx < m and ny >= 0 and ny < n:
            dfs((ny, nx))
    return True


cnt = 0
for i in range(m):
    for j in range(n):
        print(cnt, i, j, board)
        if dfs((j, i)):
            cnt += 1

print(cnt)
