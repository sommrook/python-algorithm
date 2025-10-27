import sys, heapq

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
INF = int(1e9)

problem = 1
while True:
    N = int(input())
    if N == 0:
        break
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    visited = [[INF for _ in range(N)] for _ in range(N)]

    visited[0][0] = arr[0][0]
    q = [[arr[0][0], 0, 0]]

    while q:
        money, x, y = heapq.heappop(q)
        if money > visited[x][y]:
            continue
        for _x, _y in zip(dx, dy):
            if 0 <= x+_x < N and 0 <= y+_y < N:
                if visited[x+_x][y+_y] > visited[x][y] + arr[x+_x][y+_y]:
                    visited[x+_x][y+_y] = visited[x][y] + arr[x+_x][y+_y]
                    heapq.heappush(q, [visited[x+_x][y+_y], x+_x, y+_y])

    print(f"Problem {problem}: {visited[N-1][N-1]}")

    problem += 1
