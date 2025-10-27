from collections import deque

N, S = map(int, input().split())

arr = list(map(int, input().split()))

result = 0
def bfs():
    global queue, result

    while queue:
        current_index, current_sum, sum_count = queue.popleft()
        if current_index == N-1:
            if sum_count > 0:
                if current_sum == S:
                    result += 1
            continue
        elif current_index < N-1:
            queue.append((current_index + 1, current_sum, sum_count))
            queue.append((current_index + 1, current_sum + arr[current_index + 1], sum_count + 1))


queue = deque()
queue.append((0, 0, 0))
queue.append((0, arr[0], 1))
bfs()
print(result)