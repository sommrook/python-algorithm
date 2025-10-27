from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    # visited[row][col][wall_break]
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append((0, 0, 0))  # row, col, wall_break
    visited[0][0][0] = 1

    while queue:
        x, y, wall = queue.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][wall]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # 이동할 수 있는 칸(0)
                if graph[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    queue.append((nx, ny, wall))

                # 벽(1)인데 아직 안 부쉈으면 부수고 이동
                elif graph[nx][ny] == 1 and wall == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][wall] + 1
                    queue.append((nx, ny, 1))

    return -1

print(bfs())
