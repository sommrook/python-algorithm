import heapq

N = int(input())
M = int(input())

INF = int(1e9)
bus = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, v = map(int, input().split())
    bus[s].append((e, v))

def get_min_value(_start):
    distances = [INF] * (N+1)
    distances[_start] = 0
    queue = []
    heapq.heappush(queue, [distances[_start], _start])

    while queue:
        dist, node = heapq.heappop(queue)

        if distances[node] < dist:
            continue

        for next_node, value in bus[node]:
            distance = dist + value
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, [distance, next_node])
    return distances


start, end = map(int, input().split())
result = get_min_value(start)
print(result[end])
