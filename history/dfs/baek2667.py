N = int(input())

graph = list()
for i in range(N):
    graph.append(list(map(int, input())))

search = [[0 for j in range(N)] for i in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

result = 0
address = []


def dfs(a, b):
    global result
    for x, y in zip(dx, dy):
        if 0 <= x+a < N and 0 <= y+b < N:
            if graph[x+a][y+b] == 1 and search[x+a][y+b] == 0:
                search[x+a][y+b] = 1
                dfs(x+a, y+b)
                result += 1


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and search[i][j] == 0:
            search[i][j] = 1
            result = 1
            dfs(i, j)
            address.append(result)

print(len(address))
address.sort()
for add in address:
    print(add)