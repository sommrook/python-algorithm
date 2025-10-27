n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF if i != j else 0 for j in range(n+1)] for i in range(n+1)]

for _ in range(m):
    s, e, p = map(int, input().split())
    graph[s][e] = min(graph[s][e], p)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()