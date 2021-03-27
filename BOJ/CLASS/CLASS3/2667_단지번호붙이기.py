from collections import deque

n = int(input())

graph = []
for _ in range(n):
    arr = list(map(int, list(input())))
    graph.append(arr)


def bfs(start, graph):
    q = deque([start])
    graph[start[0]][start[1]] = -1
    cnt = 0
    # 하 우 상 좌
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # print(q)

    while len(q) != 0:
        node = q.popleft()
        cnt += 1
        graph[node[0]][node[1]] = -1

        for i in range(4):
            if dx[i]+node[0] >= 0 and dx[i]+node[0] < n and dy[i]+node[1] >= 0 and dy[i]+node[1] < n:  # 미로 내부
                x = dx[i]+node[0]
                y = dy[i]+node[1]
                if graph[x][y] == 1 and (x, y) not in q:  # 방문한적 없음 and 방문예정도 없음
                    q.append((x, y))
    return cnt


answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer.append(bfs((i, j), graph))

answer.sort()
print(len(answer))
for a in answer:
    print(a)
