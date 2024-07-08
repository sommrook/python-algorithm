from collections import deque

N, K = map(int, input().split())

queue = deque()
search = [0] * 100001

fast_time = -1
count = -1

def bfs():
    global fast_time
    global count
    while queue:
        now = queue.popleft()
        # 순서가 보장 되므로, fast_time 보다 큰 시간이 나오면 break
        if 0 <= fast_time < search[now]:
            break
        if now == K:
            if fast_time == -1:
                fast_time = search[now]
                count = 1
            elif 0 <= fast_time == search[now]:
                count += 1
        for i in (now+1, now-1, now*2):
            if 0 <= i <= 100000 and (search[i] == 0 or search[i] == search[now]+1):
                queue.append(i)
                search[i] = search[now] + 1


queue.append(N)
bfs()
print(fast_time)
print(count)