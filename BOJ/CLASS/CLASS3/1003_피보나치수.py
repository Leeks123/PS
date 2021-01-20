t = int(input())

arr = []
for _ in range(t):
    arr.append(int(input()))

answer = []
for i in range(max(arr)+1):
    if i == 0:
        answer.append([1, 0])
    elif i == 1:
        answer.append([0, 1])
    else:
        answer.append([answer[i-1][0]+answer[i-2][0],
                       answer[i-1][1]+answer[i-2][1]])

for i in arr:
    print(str(answer[i][0])+' '+str(answer[i][1]))
