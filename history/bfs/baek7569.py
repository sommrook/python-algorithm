import sys
from collections import deque

M, N, H = map(int, input().split())

graph_map = dict()
for h in range(H):
    arr = list()
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    graph_map[h] = arr

visited_map = dict()
for h in range(H):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited_map[h] = visited

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dz = [-1, 1]

def get_days(que):
    while que:
        _h, _m, _n = que.popleft()
        for x, y in zip(dx, dy):
            if 0 <= _m+x < M and 0 <= _n+y <N:
                if visited_map[_h][_n+y][_m+x] == 0:
                    visited_map[_h][_n+y][_m+x] = visited_map[_h][_n][_m] + 1
                    que.append((_h, _m+x, _n+y))
        for z in dz:
            if 0 <= _h+z < H:
                if visited_map[_h+z][_n][_m] == 0:
                    visited_map[_h+z][_n][_m] = visited_map[_h][_n][_m] + 1
                    que.append((_h+z, _m, _n))

    # 0 이 존재 하는지 확인
    max_cnt = 0
    for hh in range(H):
        max_cnt = max(max_cnt, max(map(max, visited_map[hh]))-1)
        if any(0 in v for v in visited_map[hh]):
            print(-1)
            sys.exit()
    print(max_cnt)

queue = deque([])
for h in range(H):
    for n in range(N):
        for m in range(M):
            arr = graph_map[h]
            if arr[n][m] == -1:
                visited_map[h][n][m] = -1
            if arr[n][m] == 1:
                visited_map[h][n][m] = 1
                queue.append((h, m, n))

get_days(queue)

