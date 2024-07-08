from collections import deque

R, C = map(int, input().split())

# 2차 배열 에서 1차는 y축, 2차가 x 축 (행렬로 따지면)
graph = list()
for i in range(R):
    graph.append(list(map(str, input())))


queue = deque()

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def global_count(func):
    def wrapper():
        return func(count=1)
    return wrapper


@global_count
def bfs(count):
    while queue:
        a, b, alpha_list = queue.popleft()
        for x, y in zip(dx, dy):
            if 0 <= a+x < R and 0 <= b+y < C:
                if graph[a+x][b+y] not in alpha_list:
                    queue.append((a+x, b+y, alpha_list + [graph[a+x][b+y]]))
                    count = max(count, len(alpha_list) + 1)
    return count


max_count = 1
queue.append((0, 0, [graph[0][0]]))
print(bfs())