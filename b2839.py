from collections import deque

N = int(input())
packs = [3, 5]

# 다 5만 사용하거나, 다 3만 사용하거나, 5와 3을 섞어서 사용

arr = [0] * (N+1)

queue = deque()

def bfs():
    while queue:
        sum_kg, pack_count = queue.popleft()
        if arr[sum_kg] == 0:
            arr[sum_kg] = pack_count
        else:
            if arr[sum_kg] < pack_count:
                continue
            arr[sum_kg] = pack_count
        for pack in packs:
            if sum_kg + pack <= N:
                queue.append((sum_kg + pack, pack_count+1))


queue.append((0, 0))
bfs()
result = -1 if arr[N] == 0 else arr[N]
print(result)