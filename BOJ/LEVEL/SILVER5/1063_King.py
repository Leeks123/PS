k, s, turn = input().split()
turn = int(turn)

moves = []
for _ in range(turn):
    moves.append(input())


def chessToPos(pos):
    return [int(pos[1])-1, ord(pos[0])-65]


def posToChess(pos):
    x = pos[0]
    y = pos[1]
    return chr(y+65)+str(x+1)


d = {
    'R': (1, 0),
    'L': (-1, 0),
    'T': (0, 1),
    'B': (0, -1),
    'RT': (1, 1),
    'RB': (1, -1),
    'LT': (-1, 1),
    'LB': (-1, -1)
}

kingPos = chessToPos(k)
stonePos = chessToPos(s)


def canGo(cur, move):
    x = cur[0] + move[1]
    y = cur[1] + move[0]
    if x >= 0 and y >= 0 and x < 8 and y < 8:
        return True
    return False


def moving(pos, move):
    x, y = pos
    dy, dx = move
    return [x+dx, y+dy]


for move in moves:
    # print(kingPos, stonePos)
    if canGo(kingPos, d[move]):
        if moving(kingPos, d[move]) == stonePos:  # king이 이동한 곳에 Stone이 있다?
            if canGo(stonePos, d[move]):
                kingPos = moving(kingPos, d[move])
                stonePos = moving(stonePos, d[move])
        else:
            kingPos = moving(kingPos, d[move])

print(posToChess(kingPos))
print(posToChess(stonePos))
