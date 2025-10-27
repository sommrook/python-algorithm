import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)]
queue = deque()
answer = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1


for i in range(1, N+1):
    if inDegree[i] == 0:
        queue.append(i)


while queue:
    v = queue.popleft()
    answer.append(v)
    for i in graph[v]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)


print(*answer)