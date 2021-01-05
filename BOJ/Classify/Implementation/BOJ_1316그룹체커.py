n = int(input())
str = []
for _ in range(n):
    str.append(input())

def groupCheck(s):
    q = [s[0]]
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            if s[i+1] in q:
                return False
            q.append(s[i+1])
    return True

answer = 0
for s in str:
    if groupCheck(s):
        answer+=1

print(answer)