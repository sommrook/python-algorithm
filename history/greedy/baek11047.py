N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]

coins.reverse()

quot = 0
remain = K
for coin in coins:
    quot += remain // coin
    remain = remain % coin
    if remain == 0:
        break

print(quot)