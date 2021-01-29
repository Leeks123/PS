import sys

n = int(input())

conferences = []
for _ in range(n):
    s, e = list(map(int, sys.stdin.readline().split(' ')))
    conferences.append((s, e))

conferences.sort()
conferences = sorted(conferences, key=lambda conference: conference[1])

answer = 1
lastConferenceTime = conferences[0][1]
for i in range(1, len(conferences)):
    if conferences[i][0] >= lastConferenceTime:
        lastConferenceTime = conferences[i][1]
        answer += 1
        # print(conferences[i][0], lastConferenceTime)

print(answer)
