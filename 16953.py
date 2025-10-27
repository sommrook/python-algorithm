import heapq

A, B = map(int, input().split())

def bfs():
    while queue:
        cnt, now = heapq.heappop(queue)
        if now == A:
            return cnt
        if now == 0 or now == 1:
            break
        if (now-1) % 10 == 0:
            next_value = int(((now-1)/10))
            heapq.heappush(queue, (cnt+1, next_value))
        if now % 2 == 0:
            next_value = int(now/2)
            heapq.heappush(queue, (cnt+1, next_value))

    return -1


queue = []
heapq.heappush(queue, (1, B))
print(bfs())