n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

answer = []
stack = []
currentNum = 1


def push():
    global currentNum
    answer.append("+")
    stack.append(currentNum)
    currentNum += 1


def pop():
    if len(stack) != 0:
        answer.append("-")
        stack.pop()


isSuccess = True

for i in arr:
    if i in stack:
        if i == stack[-1]:
            pop()
        else:
            isSuccess = False
            break
    else:
        while True:
            if i not in stack:
                push()
            else:
                break
        pop()

if isSuccess:
    for a in answer:
        print(a)
else:
    print("NO")
