from collections import deque

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[j][i] = 1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

def bfs(queue):
    area = 1
    while queue:
        r, c = queue.popleft()
        for _x, _y in zip(dx, dy):
            if 0 <= r+_x < m and 0 <= c+_y < n:
                if graph[r+_x][c+_y] == 0 and visited[r+_x][c+_y] == 0:
                    queue.append((r+_x, c+_y))
                    visited[r+_x][c+_y] = 1
                    area += 1

    return area


result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            if visited[i][j] == 0:
                queue = deque([(i, j)])
                visited[i][j] = 1
                area = bfs(queue)
                count += 1
                result.append(area)


print(count)
result.sort()
print(*result)