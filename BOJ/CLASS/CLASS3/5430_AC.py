t = int(input())

answer = []
for _ in range(t):
    p = input()
    n = int(input())
    arr = input().split('[')[1].split(']')[0].split(',')
    if arr == ['']:
        arr = []

    front = 0
    back = 0
    isReversed = False
    for i in range(len(p)):
        if p[i] == 'R':
            isReversed = not isReversed
        if p[i] == 'D':
            if isReversed:
                back += 1
            else:
                front += 1

    if front+back > n:
        answer.append('error')
    else:
        if isReversed:
            arr.reverse()
            answer.append(arr[back:n-front])
        else:
            answer.append(arr[front:n-back])

for a in answer:
    if a == 'error':
        print(a)
    else:
        print('[', end='')
        print(','.join(a), end='')
        print(']')
