
def isBalanced(sentence):
    stack = []
    for s in sentence:
        if s == "(" or s == "[":
            stack.append(s)

        if s == ")":
            if len(stack) == 0:
                return False
            if stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif s == "]":
            if len(stack) == 0:
                return False
            if stack[-1] == "[":
                stack.pop()
            else:
                return False
    return True if len(stack) == 0 else False


answer = []
while True:
    s = input()
    if s == ".":
        break
    if isBalanced(s):
        answer.append("yes")
    else:
        answer.append("no")

for a in answer:
    print(a)
