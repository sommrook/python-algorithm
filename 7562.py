import sys
import heapq

input = sys.stdin.readline

T = int(input())

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
INF = float('inf')

def bfs(visited, queue, goal, n):
    while queue:
        count, x, y = heapq.heappop(queue)
        if x == goal[0] and y == goal[1]:
            break
        for _x, _y in zip(dx, dy):
            if 0 <= _x+x < n and 0 <= _y+y < n:
                if visited[_x+x][_y+y] > count + 1:
                    visited[_x+x][_y+y] = count + 1
                    heapq.heappush(queue, (count+1, _x+x, y+_y))


for _ in range(T):
    I = int(input())
    start = list(map(int, input().split()))
    goal = list(map(int, input().split()))
    visited = [[INF for _ in range(I)] for _ in range(I)]
    queue = []
    heapq.heappush(queue, (0, start[0], start[1]))
    visited[start[0]][start[1]] = 0
    bfs(visited, queue, goal, I)
    print(visited[goal[0]][goal[1]])

