from collections import deque

n, m = map(int, input().split())

goal = [-1, -1]
graph = []
INF = float('inf')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[INF for _ in range(m)] for _ in range(n)]
for i in range(n):
    a = list(map(int, input().split()))
    if 2 in a:
        goal = [i, a.index(2)]
    all_a_index = list(filter(lambda x: a[x] == 0, range(len(a))))
    for j in all_a_index:
        visited[i][j] = 0
    graph.append(a)

visited[goal[0]][goal[1]] = 0

def bfs():
    global queue, visited
    while queue:
        i, j, cnt = queue.popleft()
        for x, y in zip(dx, dy):
            if 0 <= i+x < n and 0 <= j+y < m:
                if graph[i+x][j+y] == 1:
                    if visited[i+x][j+y] > cnt+1:
                        visited[i+x][j+y] = cnt+1
                        queue.append((i+x, j+y, cnt+1))


queue = deque()
queue.append((goal[0], goal[1], 0))
bfs()

for i in range(n):
    for j in range(m):
        print(visited[i][j] if visited[i][j] != INF else -1, end=' ')
    print()
