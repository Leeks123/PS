n = int(input())

stair = [int(input()) for _ in range(n)]
# stair = [0]+stair
s = [0, ]


def dp():
    s.append(stair[0])
    if n == 1:
        return
    s.append(stair[0] + stair[1])
    if n == 2:
        return
    s.append(max(stair[2]+stair[1], stair[2]+stair[0]))
    if n == 3:
        return
    s.append(max(stair[3]+stair[1]+stair[0], stair[3]+stair[2]+stair[0]))
    if n == 4:
        return

    for i in range(5, n+1):
        # print(i)
        s.append(
            max(
                stair[i-1] + s[i-2],
                stair[i-1] + stair[i-2] + s[i-3],
                stair[i-1] + stair[i-3] + s[i-4],
            )
        )


dp()
print(s[-1])
