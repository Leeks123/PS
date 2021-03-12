
board = [list(map(int, input().split())) for _ in range(5)]
check = [[False]*5 for _ in range(5)]
read = [list(map(int, input().split())) for _ in range(5)]


def checkBoard(n):
    for i in range(len(board)):
        for j in range(len(board)):
            if n == board[i][j]:
                check[i][j] = True
                return


def checkBingo():
    global check
    cnt = 0
    # 가로 체크
    for row in check:
        if False in row:
            continue
        cnt += 1

    # 세로 체크
    for col in range(len(check)):
        for row in range(len(check)):
            if check[row][col] == False:
                break
            if row == 4:
                cnt += 1
    # 대각선 체크
    for i in range(len(check)):
        if check[i][i] == False:
            break
        if i == 4:
            cnt += 1
    for i in range(len(check)):
        if check[len(check)-i-1][i] == False:
            break
        if i == 4:
            cnt += 1
    return cnt


answer = 0
for i in range(len(read)):
    for j in range(len(read)):
        checkBoard(read[i][j])
        if checkBingo() >= 3:
            answer = i*5+j+1
            break
    if answer != 0:
        break

print(answer)
