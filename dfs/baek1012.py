import sys
sys.setrecursionlimit(10**6)

TC = int(input())

# M이 가로, N이 세로 (m, n) => graph[n][m]
# dic_tc = dict()

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dfs(a, b):
    search[a][b] = 1

    for x, y in zip(dx, dy):
        if 0 <= x+a < N and 0 <= y+b < M:
            if search[x+a][y+b] == 0 and graph[x+a][y+b] == 1:
                dfs(x+a, y+b)


for i in range(TC):
    M, N, K = map(int, input().split())
    result = 0

    graph = [[0 for m in range(M)] for n in range(N)]

    search = [[0 for m in range(M)] for n in range(N)]

    for j in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for nx in range(N):
        for mx in range(M):
            if search[nx][mx] == 0 and graph[nx][mx] == 1:
                result += 1
                dfs(nx, mx)

    print(result)

