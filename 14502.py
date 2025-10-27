import copy

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def spread(board, x, y):
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                spread(board, nx, ny)

def wall(count):
    global max_value
    if count == 3:
        temp = copy.deepcopy(graph)
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    spread(temp, i, j)
        safe = sum(row.count(0) for row in temp)
        max_value = max(max_value, safe)
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(count+1)
                graph[i][j] = 0  # 원상복구


max_value = 0
wall(0)
print(max_value)
