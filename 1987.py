R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
max_cnt = 1

def bfs(row, col):
    global graph, max_cnt

    q = {(row, col, graph[row][col])}  # set로 변경
    while q:
        row, col, alpha = q.pop()  # pop으로 변경
        max_cnt = max(max_cnt, len(alpha))
        for x, y in zip(dx, dy):
            nr = row + x
            nc = col + y
            if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] not in alpha:
                q.add((nr, nc, alpha + graph[nr][nc]))  # add로 변경


bfs(0, 0)
print(max_cnt)
