# 최단 거리와 비슷한 문제 => visited 여부를 꼭 체크 할것!

from collections import deque

N, K = map(int, input().split())

queue = deque()
search = [0] * 100001

def bfs():
    while queue:
        now = queue.popleft()
        if now == K:
            print(search[now])
            break
        for i in (now+1, now-1, now*2):
            if 0 <= i <= 100000 and search[i] == 0:
                queue.append(i)
                search[i] = search[now] + 1


queue.append(N)
bfs()