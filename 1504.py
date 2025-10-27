import sys
import heapq

INF = float('inf')

def solution(start):
    visited = [INF for _ in range(n + 1)]
    heap = []
    heapq.heappush(heap, [0, start])
    visited[start] = 0
    while heap:
        dist, num = heapq.heappop(heap)

        if dist > visited[num]:
            continue

        for i, j in graph[num]:
            cost = dist + j

            if cost < visited[i]:
                visited[i] = cost
                heapq.heappush(heap, [cost, i])

    return visited


n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
v1, v2 = map(int, sys.stdin.readline().split())

a = solution(1)
b = solution(v1)
c = solution(v2)

answer = min(a[v1] + b[v2] + c[n], a[v2] + c[v1] + b[n])

if answer >= INF:
    print(-1)
else:
    print(answer)