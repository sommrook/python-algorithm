import sys
from collections import deque

# BFS로 구현해보자
# sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = list()
for i in range(n):
    graph.append(list(map(int, input().split())))

draw = []

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

search = [[0 for i in range(0, m)] for j in range(0, n)]

def dfs(r, c, now_count):
    # 깊이 우선 탐색 => stack, 재귀 함수
    for x, y in zip(dx, dy):
        # (0, 0) 일 때에는 -1로 갈 수 있음 => 이를 방지 하기 위함
        if 0 <= r + x < n and 0 <= c + y < m:
            if search[r+x][c+y] == 0:
                search[r+x][c+y] = 1
                if graph[r+x][c+y] == 1:
                    now_count.append(1)
                    dfs(r+x, c+y, now_count)


def bfs(r, c):
    queue = deque()
    now_count = 1
    queue.append((r, c))
    # 자식 검사
    while queue:
        (r, c) = queue.popleft()
        for x, y in zip(dx, dy):
            if 0 <= r + x < n and 0 <= c + y < m:
                if search[r + x][c + y] == 0:
                    search[r + x][c + y] = 1
                    if graph[r+x][c+y] == 1:
                        now_count += 1
                        queue.append((r+x, c+y))
    return now_count


for row in range(0, len(graph)):
    for column in range(0, len(graph[row])):
        if search[row][column] == 0:
            search[row][column] = 1
            if graph[row][column] == 0:
                continue
            # draw.append(bfs(row, column))
            # 현재 위치 graph가 1일 때에만 실행
            count = [1]
            dfs(row, column, count)
            draw.append(len(count))

if draw:
    print(len(draw))
    print(max(draw))
else:
    print(0)
    print(0)
