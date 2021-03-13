c, r = map(int, input().split())
k = int(input())

board = [[0]*c for _ in range(r)]

#     하좌 상 우
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direction = 0
x, y = 0, 0
ticket = 1

while True:
    if ticket == c*r:
        break
    if ticket == k:
        break
    board[x][y] = ticket
    ticket += 1
    if x+dx[direction] >= 0 and y+dy[direction] >= 0 and x+dx[direction] < r and y+dy[direction] < c and board[x+dx[direction]][y+dy[direction]] == 0:
        x += dx[direction]
        y += dy[direction]
    else:
        direction = (direction + 1) % 4
        x += dx[direction]
        y += dy[direction]

if ticket == k:
    print(y+1, x+1)
else:
    print(0)
