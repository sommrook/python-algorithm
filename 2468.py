from collections import deque

N = int(input())

max_height = 0
safe_max_count = 1
graph = []
visited = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    temp = list(map(int, input().split()))
    max_height = max(max_height, max(temp))
    graph.append(temp)

queue = deque()

def bfs(_h):
    while queue:
        _row, _col = queue.popleft()
        for x, y in zip(dx, dy):
            if 0 <= _row + x < N and 0 <= _col + y < N:
                if visited[_row+x][_col+y] == 0 and graph[_row+x][_col+y] > _h:
                    visited[_row+x][_col+y] = 1
                    queue.append((_row+x, _col+y))


# 최댓값보단 항상 작아야함 : 최댓값일때에는 모두 잠겨버려서 0이 된다.
for h in range(1, max_height):
    visited = [[0] * N for _ in range(N)]
    result = 0
    for row in range(N):
        for col in range(N):
            if graph[row][col] > h and visited[row][col] == 0:
                queue.append((row, col))
                visited[row][col] = 1
                bfs(h)
                result += 1

    safe_max_count = max(safe_max_count, result)

print(safe_max_count)