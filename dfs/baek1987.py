from collections import deque

R, C = map(int, input().split())

# 2차 배열 에서 1차는 y축, 2차가 x 축 (행렬로 따지면)
graph = list()
for i in range(R):
    graph.append(list(map(str, input())))


already = deque()

max_count = 1

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def dfs(a, b, count):
    global max_count
    max_count = max(max_count, count)

    for x, y in zip(dx, dy):
        if 0 <= x+a < R and 0 <= y+b < C:
            if graph[x+a][y+b] not in already:
                already.append(graph[x+a][y+b])
                # 자식 -> 부모 + 1
                dfs(x+a, y+b, count+1)
                # 자식 순회가 끝난 후 => 즉 더이상 갈 수 있는 알파 벳이 없다.
                already.remove(graph[x+a][y+b])


already.append(graph[0][0])
dfs(0, 0, 1)

print(max_count)