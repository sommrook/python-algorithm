from collections import deque

R, C = map(int, input().split())

# 2차 배열 에서 1차는 y축, 2차가 x 축 (행렬로 따지면)
graph = list()
for i in range(R):
    graph.append(list(map(str, input())))


queue = deque()

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def bfs():
    global max_count

    while queue:
        a, b, alpha_list = queue.popleft()
        for x, y in zip(dx, dy):
            if 0 <= a+x < R and 0 <= b+y < C:
                if graph[a+x][b+y] not in alpha_list:
                    queue.append((a+x, b+y, alpha_list + [graph[a+x][b+y]]))
                    max_count = max(max_count, len(alpha_list) + 1)


max_count = 1
queue.append((0, 0, [graph[0][0]]))
bfs()
print(max_count)