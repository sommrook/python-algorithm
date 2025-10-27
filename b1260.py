from collections import deque

N, M, V = map(int, input().split())
lines = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    start, end = map(int, input().split())
    lines[start].append(end)
    if start not in lines[end]:
        lines[end].append(start)

lines = {key: sorted(value) for key, value in lines.items()}
dfs_stores = []
bfs_stores = []

def dfs(n):
    if n not in dfs_stores:
        dfs_stores.append(n)
        for i in lines[n]:
            dfs(i)


queue = deque()
def bfs():
    while queue:
        current_number = queue.popleft()
        if current_number not in bfs_stores:
            bfs_stores.append(current_number)
            for i in lines[current_number]:
                queue.append(i)


dfs(V)
print(" ".join(map(str, dfs_stores)))
queue.append(V)
bfs()
print(" ".join(map(str, bfs_stores)))
