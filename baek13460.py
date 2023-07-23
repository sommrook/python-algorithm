"""
https://www.acmicpc.net/problem/13460
"""

"""
핵심: 한번 기울일때마다 한칸씩 움직이는 것이 아니라, 한번에 가는것!
"""
from collections import deque

N, M = map(int, input().split())

graph = [list(map(str, input())) for _ in range(N)]

# red_visited = [[0 if j != 0 and j != M - 1 else 1 for j in range(M)] if i != 0 and i != N - 1 else [1] * M for i in
#                range(N)]

visited = []

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

queue = deque()


def bfs():
    while queue:
        red_n, red_m, blue_n, blue_m, count = queue.popleft()
        # print(f"[{red_n}][{red_m}] and [{blue_n}][{blue_m}]")
        if count >= 10:
            return -1

        for r, c in zip(dx, dy):
            if 0 <= red_n + r < N and 0 <= red_m + c < M:
                move_red_n = red_n + r
                move_red_m = red_m + c
                move_blue_n = blue_n + r
                move_blue_m = blue_m + c
                # 고려 -> 옆에 '#'이 있는지 -> X / 옆에 'B'가 있는지 -> 'A'가 옮겼을 때 'B'와 겹치는지?
                # red랑 blue를 따로..
                # red
                move_red = 0
                move_blue = 0
                while True:
                    if 0 <= move_red_n < N and 0 <= move_red_m < M:
                        if graph[move_red_n][move_red_m] == '#':
                            move_red_n = move_red_n - r
                            move_red_m = move_red_m - c
                            break
                        elif graph[move_red_n][move_red_m] == 'O':
                            move_red += 1
                            break
                        else:
                            # red_visited[move_red_n][move_red_m] = 1
                            move_red_n = move_red_n + r
                            move_red_m = move_red_m + c
                            move_red += 1
                while True:
                    if 0 <= move_blue_n < N and 0 <= move_blue_m < M:
                        if graph[move_blue_n][move_blue_m] == '#':
                            move_blue_n = move_blue_n - r
                            move_blue_m = move_blue_m - c
                            break
                        elif graph[move_blue_n][move_blue_m] == 'O':
                            move_blue += 1
                            break
                        else:
                            move_blue_n = move_blue_n + r
                            move_blue_m = move_blue_m + c
                            move_blue += 1
                # 1. red가 O이면 -> blue가 O인지 아닌지 체크
                # 2. 둘이 같으면 -> 더 많이 움직인 애가 뒤로 와야함
                # 3. move_red가 0이면 queue에 담지 않음
                if not (move_red == 0 and move_blue == 0):
                    if graph[move_blue_n][move_blue_m] == 'O':
                        continue
                    if graph[move_red_n][move_red_m] == 'O':
                        return count + 1
                    if move_red_n == move_blue_n and move_red_m == move_blue_m:
                        if move_red > move_blue:
                            move_red_n = move_red_n - r
                            move_red_m = move_red_m - c
                        else:
                            move_blue_n = move_blue_n - r
                            move_blue_m = move_blue_m - c
                    if (move_red_n, move_red_m, move_blue_n, move_blue_m) not in visited:
                        visited.append((move_red_n, move_red_m, move_blue_n, move_blue_m))
                        queue.append((move_red_n, move_red_m, move_blue_n, move_blue_m, count + 1))

    return -1


blue = (0, 0, 'B', 0)
red = (0, 0, 'R', 0)
for n in range(1, N):
    for m in range(1, M):
        if graph[n][m] == 'B':
            graph[n][m] = '.'
            blue = (n, m)
        elif graph[n][m] == 'R':
            graph[n][m] = '.'
            red = (n, m)
            # red_visited[n][m] = 1

visited.append((red[0], red[1], blue[0], blue[1]))
queue.append((red[0], red[1], blue[0], blue[1], 0))
print(bfs())
