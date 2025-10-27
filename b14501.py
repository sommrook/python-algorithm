from collections import deque

N = int(input())

dp = [0] * (N+1)
counsel = {}

for i in range(N):
    counsel[i+1] = list(map(int, input().split()))

queue = deque()

def bfs():
    while queue:
        history, current_price = queue.popleft()
        init_start_counsel = history[-1] + counsel[history[-1]][0]
        # print(f"pop history: {history}, init_start_counsel: {init_start_counsel}, current_price: {current_price}")

        for start_counsel in range(init_start_counsel, N+1):
            # start_counsel price 더해주고 history에 넣어주고 등등..
            end_counsel = start_counsel + counsel[start_counsel][0] - 1
            if end_counsel <= N and start_counsel not in history and dp[end_counsel] < counsel[start_counsel][1] + current_price:
                # print(f"end_counsel: {end_counsel}, start_counsel: {start_counsel}, current_price: {current_price}")
                dp[end_counsel] = counsel[start_counsel][1] + current_price
                # print(f"dp[end_counsel]:{dp[end_counsel]}")
                queue.append((history+[start_counsel], counsel[start_counsel][1] + current_price))


for i in range(1, N+1):
    days = counsel[i][0]
    price = counsel[i][1]
    if i+days-1 <= N and dp[i+days-1] < price:
        queue.append(([i], price))
        dp[i+days-1] = price

bfs()
print(max(dp))