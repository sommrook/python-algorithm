from collections import deque

V, E = map(int, input().split())

# value에 여러개의 tuple쌍이 있을 수 있다.
# graph = {i+1: [] for i in range(V)}
graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
start_position = int(input())
dp = [0] * (V+1)
# visited = [[0 for _ in range(V+1)] for _ in range(V+1)]

# min_value = 0

for _ in range(E):
    start, end, value = map(int, input().split())
    if graph[start][end] == 0:
        graph[start][end] = value
    else:
        graph[start][end] = min(graph[start][end], value)


def set_graph(_e, _v):
    graph[start_position][_e] = min(graph[start_position][_e], _v)


def bfs(_end):
    global max_value

    queue = deque()
    for v in range(1, V+1):
        if start_position != v and graph[start_position][v] != 0:
            queue.append((start_position, v, graph[start_position][v]))
            visited[start_position][v] = 1

    while queue:
        _s, _e, _v = queue.popleft()
        if _e == _end:
            if min_value == -1:
                min_value = _v
            else:
                min_value = min(min_value, _v)
            continue

        for v in range(1, V+1):
            if graph[_e][v] != 0 and visited[_e][v] == 0:
                queue.append((v, _e, graph[_e][v]+_v))
                visited[_e][v] = 1


for i in range(1, V+1):
    if start_position == i:
        print(0)
    else:
        visited = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
        max_value = -1
        bfs(i)
        if max_value == -1:
            print("INF")
        else:
            print(max_value)
            set_graph(i, max_value)