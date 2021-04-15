def isPalindrome(arr):
    for i in range(len(arr)//2):
        if arr[i] != arr[len(arr)-i-1]:
            return False
    return True


def countPalindrome(board):
    ret = 0
    for arr in board:
        for n in range(100, 1, -1):
            for i in range(100 - n + 1):
                if isPalindrome(arr[i:i+n]):
                    if ret < n:
                        ret = n
    return ret


def rotateBoard(board):
    ret = []
    for i in range(100):
        arr = []
        for j in range(100):
            arr.append(board[j][i])
        ret.append(arr)
    return ret


def solve():
    n = int(input())
    board = []
    for _ in range(100):
        board.append(list(input()))
    answer = countPalindrome(board)
    board = rotateBoard(board)
    answer2 = countPalindrome(board)
    return max(answer, answer2)


for i in range(1, 11):
    answer = solve()
    print('#'+str(i), answer)
