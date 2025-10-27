from collections import deque

N, L, R = map(int, input().split())
arr = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(N):
    arr.append(list(map(int, input().split())))

queue = deque([])

def bfs(union, result):
    while queue:
        r, c = queue.popleft()
        for _x, _y in zip(dx, dy):
            next_row = r + _x
            next_col = c + _y
            if 0 <= next_row < N and 0 <= next_col < N and visited[next_row][next_col] == 0:
                if L <= abs(arr[next_row][next_col] - arr[r][c]) <= R:
                    queue.append((next_row, next_col))
                    result += arr[next_row][next_col]
                    union.append((next_row, next_col))
                    visited[next_row][next_col] = 1

    if len(union) == 1:
        return False

    new_result = result // cnt
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 1:
                arr[r][c] = new_result
                visited[r][c] = -1
    return True


transfer = 0
while True:
    moved = False
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                result = arr[i][j]
                cnt = 1
                queue.append((i, j))
                res = bfs(result, cnt)
                if res:
                    moved = True

    if not moved:
        break

    transfer += 1


print(transfer)