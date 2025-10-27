import sys, heapq
input = sys.stdin.readline
# N: 도시 갯수
# M: 간선 갯수
# K: 구해야하는 거리 정보
# X: 출발 정보
N, M, K, X = map(int, input().split())

INF = 1e9
city = {key+1: [] for key in range(N)}
visited = [INF] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    city[A].append(B)

def dijkstra(start):
    queue = [(0, start)]
    while queue:
        cost, node = heapq.heappop(queue)
        if cost > visited[node]:
            continue
        for next_node in city[node]:
            if visited[next_node] > cost + 1:
                visited[next_node] = cost + 1
                heapq.heappush(queue, (cost + 1, next_node))


visited[X] = 0
dijkstra(X)
temp = 0
for i in range(1, N+1):
    if visited[i] == K:
        temp += 1
        print(i)

if temp == 0:
    print(-1)