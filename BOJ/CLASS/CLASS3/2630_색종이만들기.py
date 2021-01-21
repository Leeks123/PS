n = int(input())

full = []
white = []
blue = []

for i in range(n):
    s = list(map(int, input().split()))
    full.append(s)


def isFill(paper):
    init = paper[0][0]
    for i in range(len(paper)):
        for j in range(len(paper)):
            if paper[i][j] != init:
                return False
    return True


def paperCut(paper):
    one = []
    two = []
    thr = []
    fou = []
    if len(paper) % 2 == 0:
        for i in range(len(paper)//2):
            tmp = []
            for j in range(len(paper)//2):
                tmp.append(paper[i][j])
            one.append(tmp)
        for i in range(len(paper)//2):
            tmp = []
            for j in range(len(paper)//2, len(paper)):
                tmp.append(paper[i][j])
            two.append(tmp)
        for i in range(len(paper)//2, len(paper)):
            tmp = []
            for j in range(len(paper)//2):
                tmp.append(paper[i][j])
            thr.append(tmp)
        for i in range(len(paper)//2, len(paper)):
            tmp = []
            for j in range(len(paper)//2, len(paper)):
                tmp.append(paper[i][j])
            fou.append(tmp)
    return one, two, thr, fou


def isWhite(paper):
    return True if paper[0][0] == 0 else False


def run(paper):
    global white
    global blue
    if isFill(paper):
        if isWhite(paper):
            white.append(paper)
        else:
            blue.append(paper)
    else:
        one, two, thr, fou = paperCut(paper)
        run(one)
        run(two)
        run(thr)
        run(fou)


run(full)

print(len(white))
print(len(blue))
