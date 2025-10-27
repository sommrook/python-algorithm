import heapq

n = int(input())
m = int(input())

bus = [[] for _ in range(n+1)]

INF = int(1e9)
for _ in range(m):
    s, e, p = map(int, input().split())
    bus[s].append((e, p))

start, end = map(int, input().split())

def get_min_distance(_start):
    distances = [INF] * (n+1)
    distances[_start] = 0
    channels = [[] for _ in range(n+1)]
    # 중복 코드 최소화를 위해 초기에 자기 자신부터
    queue = [[0, [_start]]]

    while queue:
        price, now_channel = heapq.heappop(queue)
        now_node = now_channel[-1]
        # print(price, now_channel, now_node)

        if distances[now_node] < price:
            continue

        # 이미 방문한 노드 경로는 갈 수 없다.
        # 왜냐하면 모두 양수이기 때문에 저장되어 있는 값보다 작을때만 검사 순회하기 때문
        for next_node, next_price in bus[now_node]:
            total_price = price + next_price
            temp_channel = now_channel[:] + [next_node]
            # print(total_price, temp_channel)
            if distances[next_node] > total_price:
                distances[next_node] = total_price
                channels[next_node] = temp_channel
                heapq.heappush(queue, [total_price, temp_channel])

    return distances, channels


result_distances, result_channels = get_min_distance(start)
print(result_distances[end])
print(len(result_channels[end]))
for channel in result_channels[end]:
    print(channel, end=" ")