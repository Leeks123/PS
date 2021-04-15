import math
t = int(input())


def isPalindrome(arr):
    for i in range(len(arr)//2):
        if arr[i] != arr[len(arr)-i-1]:
            return False
    return True


def isSquare(x):
    tmp = math.sqrt(x)
    if math.floor(tmp) == tmp:
        return True
    return False


def checkSquarePalin(a, b):
    cnt = 0
    for i in range(a, b+1):
        if isSquare(i):
            if isPalindrome(list(str(i))):
                tmp = int(math.sqrt(i))
                if isPalindrome(list(str(tmp))):
                    cnt += 1
    return cnt


for i in range(1, t+1):
    a, b = map(int, input().split())
    answer = checkSquarePalin(a, b)
    print('#'+str(i), answer)
