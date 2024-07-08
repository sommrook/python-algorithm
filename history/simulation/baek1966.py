from collections import deque

N = int(input())

counts = []
for _ in range(N):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(arr)
    queue = deque()
    for i, order in enumerate(arr):
        queue.append((i, order))
    # print(queue)

    arr = deque(arr)

    # index 정보
    idx = deque([0+i for i in range(n)])
    count = 0
    while queue:
        index, now_order = queue.popleft()
        # 현재 order 가 제일 큰 숫자가 아니면
        if max(arr) != now_order:
            queue.append((index, now_order))
            ord = arr.popleft()
            arr.append(ord)
        # 현재 order 가 제일 큰 숫자 이면
        else:
            arr.popleft()
            count += 1
            if index == m:
                counts.append(count)
                break


for c in counts:
    print(c)