from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

queue = deque()

"""
가로: width
세로: height
대각선: diagonal
"""
queue.append((0, 1, "width"))

count = 0
while queue:
    r, c, k = queue.popleft()
    if r == N - 1 and c == N - 1:
        count += 1
        continue
    if k != "width":
        if r+1 <= N-1 and graph[r+1][c] != 1:
            queue.append((r+1, c, "height"))
    if k != "height":
        if c+1 <= N-1 and graph[r][c+1] != 1:
            queue.append((r, c+1, "width"))
    if r+1 <= N-1 and c+1 <= N-1:
        if graph[r+1][c+1] != 1 and graph[r][c+1] != 1 and graph[r+1][c] != 1:
            queue.append((r + 1, c + 1, "diagonal"))

print(count)