from collections import deque

# N => row
# M => column
N, M = map(int, input().split())

# graph[y][x]
# graph[row][column]
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

visited = [[0 for _ in range(M)] for _ in range(N)]

queue = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while queue:
        a, b = queue.popleft()
        for x, y in zip(dx, dy):
            if 0 <= x+a < N and 0 <= y+b < M:
                if graph[x+a][y+b] == 1 and visited[x+a][y+b] == 0:
                    visited[x+a][y+b] = visited[a][b] + 1
                    if x+a == N-1 and y+b == M-1:
                        print(visited[x+a][y+b])
                        break
                    queue.append((x+a, y+b))


queue.append((0, 0))
visited[0][0] = 1
bfs()
