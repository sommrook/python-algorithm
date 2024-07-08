from collections import deque

N = int(input())

stairs = [int(input()) if i != 0 else 0 for i in range(N+1)]

queue = deque()

max_count = 0
def bfs():
    global max_count
    queue.append((0, stairs[0], []))
    while queue:
        index, count, foots = queue.popleft()
        if index == N:
            max_count = count if max_count == 0 else max(max_count, count)
        if index-1 not in foots and index+1 <= N:
            queue.append((index+1, count+stairs[index+1], foots+[index+1]))
        if index+2 <= N:
            queue.append((index+2, count+stairs[index+2], foots+[index+2]))


bfs()
print(max_count)