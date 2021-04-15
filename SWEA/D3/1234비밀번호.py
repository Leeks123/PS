def isPalindrome(arr):
    for i in range(len(arr)//2):
        if arr[i] != arr[len(arr)-i-1]:
            return False
    return True


def isDupl(arr):
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return True
    return False


def elimiate(arr, idx):
    minLen = idx if idx < len(arr)-idx-2 else len(arr)-idx-2
    for i in range(minLen+1):
        if not isPalindrome(arr[idx-i:idx+i+2]):
            return arr[0:idx-i+1] + arr[idx+i+1:]
    return arr[0:idx]+arr[idx+2:]


def solve(arr):
    while isDupl(arr):
        duplIdx = 0
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                duplIdx = i
        arr = elimiate(arr, duplIdx)
    return ''.join(arr)


for i in range(1, 11):
    n, s = input().split()
    answer = solve(list(s))
    print('#'+str(i), answer)
