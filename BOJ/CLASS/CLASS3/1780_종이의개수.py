# 런타임에러..인덱스에러
n = int(input())

paper = []
for _ in range(n):
    i = list(map(int, input().split()))
    paper.append(i)


def allSame(paper):
    if len(paper) == 1:
        return True
    else:
        init = paper[0][0]
        for r in paper:
            for c in r:
                if init != c:
                    return False
        return True


def cut(paper):
    cutted = []
    if len(paper) > 3:
        for i in range(len(paper)//3):
            tmp = []
            for j in range(len(paper)//3):
                rows = paper[len(paper)//3*i:len(paper)//3*(i+1)]
                for r in rows:
                    tmp.append(r[len(paper)//3*j:len(paper)//3*(j+1)])
                cutted.append(tmp)
                tmp = []
    else:
        for i in range(len(paper)):
            for j in range(len(paper)):
                cutted.append([[paper[i][j]]])
    return cutted


answer = [0, 0, 0]


def run(paper):
    global answer
    if allSame(paper):
        if paper[0][0] == -1:
            answer[0] += 1
        elif paper[0][0] == 0:
            answer[1] += 1
        else:
            answer[2] += 1
        return
    else:
        cutted = cut(paper)
        for c in cutted:
            run(c)


run(paper)

for a in answer:
    print(a)
