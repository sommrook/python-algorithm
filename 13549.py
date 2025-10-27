import heapq

N, K = map(int, input().split())

dp = [0] * 100001
result = 0

def bfs():
    global result
    while queue:
        time, now = heapq.heappop(queue)
        if now == K:
            result = time
            break
        if 0 <= now*2 <= 100000 and dp[now*2] == 0:
            heapq.heappush(queue, (time, now*2))
            dp[now*2] = 1
        if 0 <= now-1 <= 100000 and dp[now-1] == 0:
            heapq.heappush(queue, (time+1, now-1))
            dp[now-1] = 1
        if 0 <= now+1 <= 100000 and dp[now+1] == 0:
            heapq.heappush(queue, (time+1, now+1))
            dp[now+1] = 1


queue = []
heapq.heappush(queue, (0, N))
dp[N] = 1
bfs()

print(result)