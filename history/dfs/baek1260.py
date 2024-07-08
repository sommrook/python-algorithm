from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    _x, _y = map(int, input().split())
    graph[_x].append(_y)
    graph[_y].append(_x)

[row.sort() for row in graph]

queue = deque()

def dfs(_v):
    dfs_list.append(_v)
    visited[_v] = 1
    for x in graph[_v]:
        if visited[x] == 0:
            visited[x] = 1
            dfs(x)

def bfs(_v):
    queue.append(_v)
    visited[_v] = 1
    while queue:
        now = queue.popleft()
        bfs_list.append(now)
        for x in graph[now]:
            if visited[x] == 0:
                visited[x] = 1
                queue.append(x)


visited = [0 for _ in range(n + 1)]
dfs_list = []
dfs(v)

visited = [0 for _ in range(n + 1)]
bfs_list = []
bfs(v)

print(" ".join(map(str, dfs_list)))
print(" ".join(map(str, bfs_list)))