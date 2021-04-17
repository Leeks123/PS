from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())

board = []
viruses = []
spaces = []

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(m):
        if arr[j] == 0:
            spaces.append((i, j))
        elif arr[j] == 2:
            viruses.append((i, j))
    board.append(arr)


def bfs(inboard, start):
    board = copy.deepcopy(inboard)
    #     우 하 좌 상
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    q = deque([start])
    board[start[0]][start[1]] = -1

    while len(q) != 0:
        v = q.popleft()
        for i in range(4):
            if v[0]+dx[i] < 0 or v[0]+dx[i] >= n or v[1]+dy[i] < 0 or v[1]+dy[i] >= m:  # board 바깥
                continue
            else:
                if board[v[0]+dx[i]][v[1]+dy[i]] == 0:  # 방문하지 않음
                    board[v[0]+dx[i]][v[1]+dy[i]] = board[v[0]][v[1]] - 1
                    q.append((v[0]+dx[i], v[1]+dy[i]))
    return board


def buildWall(board, pick):
    ret = copy.deepcopy(board)
    for p in pick:
        ret[p[0]][p[1]] = 1
    return ret


def countZero(board):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1
    return cnt


# print(bfs(board, (1, 5)))
answer = 0
for pick in list(combinations(spaces, 3)):
    builded = buildWall(board, pick)

    for v in viruses:
        builded = bfs(builded, v)
    zeros = countZero(builded)
    if answer < zeros:
        answer = zeros

print(answer)
