import heapq

F, S, G, U, D = map(int, input().split())
INF = float("inf")
visited = [INF] * (F+1)

queue = []
heapq.heappush(queue, (0, S))
visited[S] = 0
while queue:
    cnt, now = heapq.heappop(queue)
    if now == G:
        break
    if 1 <= now-D <= F and visited[now-D] > cnt+1:
        heapq.heappush(queue, (cnt+1, now-D))
        visited[now-D] = cnt+1
    if 1 <= now+U <= F and visited[now+U] > cnt+1:
        heapq.heappush(queue, (cnt+1, now+U))
        visited[now+U] = cnt+1

print(visited[G] if visited[G] != INF else "use the stairs")