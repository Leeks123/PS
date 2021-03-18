from collections import deque

n, m = map(int, input().split())
findThings = list(map(int, input().split()))

queue = deque([x for x in range(1, n+1)])

answer = 0
for f in findThings:
    # print(queue)
    findIdx = queue.index(f)
    # print(findIdx, answer)
    if findIdx == 0:
        queue.popleft()
    elif findIdx <= (len(queue) // 2):  # 중간 이전에
        while True:
            poped = queue.popleft()
            if poped == f:
                break
            else:
                answer += 1
                queue.append(poped)
    else:  # 중간 이후에
        while True:
            poped = queue.pop()
            if poped == f:
                answer += 1
                break
            else:
                answer += 1
                queue.appendleft(poped)

print(answer)
