# M => width(column x) / N => height(row y)
# 1 -> 익은 토마토
# 0 -> 익지 않은 토마토 (하루가 지나면 익은 토마토 에 인접해 있으면 익게 된다.)
# -1 -> 토마토 X

from collections import deque

M, N = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# visited = [[0 for _ in range(M)] for _ in range(N)]

max_count = 0
queue = deque()

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs():
    global max_count
    while queue:
        a, b, count = queue.popleft()
        max_count = max(count, max_count)
        for _x, _y in zip(dx, dy):
            if 0 <= _x+a < N and 0 <= _y+b < M:
                if graph[_x+a][_y+b] == 0:
                    # visited[_x+a][_y+b] = visited[a][b] + 1
                    graph[_x+a][_y+b] = 1
                    queue.append((_x+a, _y+b, count+1))

    for _n in range(N):
        if 0 in graph[_n]:
            return -1
    return max_count


complete_flag = 0
fail = 0
for x in range(N):
    for y in range(M):
        if graph[x][y] == 1:
            queue.append((x, y, 0))
            complete_flag += 1
        elif graph[x][y] == -1:
            complete_flag += 1


if complete_flag == N*M:
    print(0)
else:
    # 1인 애들 다 모아서 시작
    print(bfs())