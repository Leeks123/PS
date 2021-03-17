import math
t = int(input())


def getDistance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if getDistance(x1, y1, x2, y2) == 0:  # 동일좌표
        if r1 == r2:  # 동일크기
            print(-1)
        else:  # 다른 크기
            print(0)
    else:
        if getDistance(x1, y1, x2, y2) == r1-r2 or getDistance(x1, y1, x2, y2) == r2-r1:  # 내접
            print(1)
        elif getDistance(x1, y1, x2, y2) < r1-r2 or getDistance(x1, y1, x2, y2) < r2-r1:  # 내부에 있음
            print(0)
        elif getDistance(x1, y1, x2, y2) == r1+r2:  # 외접
            print(1)
        elif getDistance(x1, y1, x2, y2) < r1+r2:  # 겹침
            print(2)
        elif getDistance(x1, y1, x2, y2) > r1+r2:
            print(0)
