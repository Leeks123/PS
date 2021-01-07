n, m = map(int, input().split())

board = []*n

for _ in range(n):
    board.append(list(input()))

odd = 'WBWBWBWB'
even = 'BWBWBWBW'
chess1 = [
    list(odd), list(even),
    list(odd), list(even),
    list(odd), list(even),
    list(odd), list(even),
]
chess2 = [
    list(even), list(odd),
    list(even), list(odd),
    list(even), list(odd),
    list(even), list(odd),
]


def countFill(board):
    cnt1 = 0
    cnt2 = 0
    for i in range(8):
        for j in range(8):
            if chess1[i][j] != board[i][j]:
                cnt1 += 1
            if chess2[i][j] != board[i][j]:
                cnt2 += 1

    return min(cnt1, cnt2)


def slice2Darr(n, m):
    ret = []
    for i in range(n, n+8):
        ret.append(board[i][m:m+8])
    return ret


answer = 64
for i in range(n-8+1):
    for j in range(m-8+1):
        answer = min(countFill(slice2Darr(i, j)), answer)

print(answer)
