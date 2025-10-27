import sys
from collections import deque

input = sys.stdin.readline

L, W = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(L)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_l, start_w):
    visited = [[-1] * W for _ in range(L)]
    q = deque([(start_l, start_w)])
    visited[start_l][start_w] = 0
    max_dist = 0

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if 0 <= nr < L and 0 <= nc < W and graph[nr][nc] == 'L' and visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                max_dist = max(max_dist, visited[nr][nc])
                q.append((nr, nc))

    return max_dist

mx = 0
for l in range(L):
    for w in range(W):
        if graph[l][w] == 'L':
            mx = max(mx, bfs(l, w))

print(mx)
