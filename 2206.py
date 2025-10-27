import heapq

N, M = map(int, input().split())
graph = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

INF = float('inf')

# 0은 이동 가능
# 1은 벽
# 하나의 벽 부셔서 최단 경로 구하기
for _ in range(N):
    R = input()
    temp = []
    for r in R:
        temp.append(int(r))
    graph.append(temp)


def bfs():
    global min_distance

    queue = []
    visited = [[INF for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    heapq.heappush(queue, (1, 0, 0))

    while queue:
        cnt, n, m = heapq.heappop(queue)
        if n == N-1 and m == M-1:
            min_distance = min(min_distance, cnt)
            break

        for x, y in zip(dx, dy):
            next_row = x+n
            next_col = y+m
            if 0 <= next_row < N and 0 <= next_col < M:
                if graph[next_row][next_col] == 0 and visited[next_row][next_col] > cnt+1:
                    visited[next_row][next_col] = cnt+1
                    heapq.heappush(queue, (cnt+1, next_row, next_col))


min_distance = INF
bfs()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            graph[i][j] = 0
            bfs()
            graph[i][j] = 1


print(min_distance if min_distance != INF else -1)