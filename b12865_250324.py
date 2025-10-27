from collections import deque

# N: 갯수
# K: 최대 weight
N, K = map(int, input().split())

arr = []
# 0: weight
# 1: value
for _ in range(N):
    arr.append(list(map(int, input().split())))

queue = deque()

max_value = 0
def bfs():
    # index, weight, value
    queue.append((0, arr[0][0], arr[0][1]))
    queue.append((0, 0, 0))
    global max_value
    # max_value = arr[0][1]
    while queue:
        index, weight, value = queue.popleft()
        if value > max_value:
            max_value = value
        if index == N-1:
            continue
        if weight+arr[index+1][0] <= K:
            queue.append((index+1, weight+arr[index+1][0], value+arr[index+1][1]))
        queue.append((index+1, weight, value))


bfs()
print(max_value)
