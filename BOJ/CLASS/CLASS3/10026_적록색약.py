import copy
import sys
sys.setrecursionlimit(100000)

n = int(input())

board = []
for _ in range(n):
    board.append(list(input()))

graph = copy.deepcopy(board)


def dfs(x, y, target):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == target:
        graph[x][y] = 1

        dfs(x-1, y, target)
        dfs(x, y-1, target)
        dfs(x+1, y, target)
        dfs(x, y+1, target)
        return True
    return False


rgbCount = 0
rbCount = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j, 'R'):
            rgbCount += 1
        if dfs(i, j, 'G'):
            rgbCount += 1
        if dfs(i, j, 'B'):
            rgbCount += 1

graph = copy.deepcopy(board)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if dfs(i, j, 'R'):
            rbCount += 1
        if dfs(i, j, 'B'):
            rbCount += 1

print(rgbCount, rbCount)
