from collections import deque

N = int(input())

max_height = 0
# 0일 때에는 count 가 1이니까 1부터 시작
max_count = 1

graph = []

for _ in range(N):
    row = list(map(int, input().split()))
    max_height = max(max_height, max(row))
    graph.append(row)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

queue = deque()

def bfs(_h):
    while queue:
        a, b = queue.popleft()
        for x, y in zip(dx, dy):
            if 0 <= a+x < N and 0 <= b+y < N:
                if visited[a+x][b+y] == 0 and graph[a+x][b+y] > _h:
                    visited[a+x][b+y] = 1
                    queue.append((a+x, b+y))


# 1부터 max_height 전까지
for h in range(1, max_height):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    h_count = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > h and visited[i][j] == 0:
                visited[i][j] = 1
                queue.append((i, j))
                h_count += 1
                bfs(h)
    max_count = max(max_count, h_count)


print(max_count)
