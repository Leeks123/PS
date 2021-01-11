def isBalanced(sentence):
    stack = []
    for s in sentence:
        if s == "(":
            stack.append(s)

        if s == ")":
            if len(stack) == 0:
                return False
            if stack[-1] == "(":
                stack.pop()
            else:
                return False
    return True if len(stack) == 0 else False


t = int(input())

answer = []
for i in range(t):
    if isBalanced(input()):
        answer.append("YES")
    else:
        answer.append("NO")

for a in answer:
    print(a)
