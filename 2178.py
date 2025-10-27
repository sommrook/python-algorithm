from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


queue = deque()
# min_count = 200
def bfs():
    global queue
    while queue:
        x, y, count = queue.popleft()
        if x == N-1 and y == M-1:
            print(count)
            break
        for i, j in zip(dx, dy):
            if 0 <= x + i < N and 0 <= y + j < M:
                if graph[x + i][y + j] == 1:
                    queue.append((x + i, y + j, count+1))
                    graph[x + i][y + j] = 0


queue.append((0, 0, 1))
graph[0][0] = 0
bfs()