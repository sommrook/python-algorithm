import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
visited = [0] * (N+1)
graph = {k: [] for k in range(N+1)}
for _ in range(M):
    s, e = map(int, input().split())
    if s not in graph:
        graph[s] = [e]
    else:
        graph[s].append(e)

    if e not in graph:
        graph[e] = [s]
    else:
        graph[e].append(s)


def bfs(queue):
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if visited[next_node] == 0:
                queue.append(next_node)
                visited[next_node] = 1


count = 0
for key in graph:
    if graph[key] and visited[key] == 0:
        visited[key] = 1
        queue = deque([key])
        bfs(queue)
        count += 1

print(count+visited.count(0)-1)