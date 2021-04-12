def isPalindrome(arr):
    for i in range(len(arr)//2):
        if arr[i] != arr[len(arr)-i-1]:
            return False
    return True


def countPalindrome(board, n):
    cnt = 0
    for arr in board:
        for i in range(8 - n + 1):
            if isPalindrome(arr[i:i+n]):
                cnt += 1
    return cnt


def rotateBoard(board):
    ret = []
    for i in range(8):
        arr = []
        for j in range(8):
            arr.append(board[j][i])
        ret.append(arr)
    return ret


def solve():
    n = int(input())
    board = []
    for _ in range(8):
        board.append(list(input()))
    answer = countPalindrome(board, n)
    board = rotateBoard(board)
    answer += countPalindrome(board, n)
    return answer


for i in range(1, 11):
    answer = solve()
    print('#'+str(i), answer)
