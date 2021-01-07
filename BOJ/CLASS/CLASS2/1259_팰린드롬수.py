
def isPalindrome(arr):
    for i in range(len(arr)//2):
        if arr[i] == arr[-1*(i+1)]:
            continue
        else:
            return False
    return True


answers = []
while True:
    n = input()
    if n == '0':
        break
    arr = list(map(int, n))
    answers.append("yes" if isPalindrome(arr) else "no")

for a in answers:
    print(a)
