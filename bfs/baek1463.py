from collections import deque

N = int(input())

visited = [0] * N

queue = deque()

def bfs():
    while queue:
        n, count = queue.popleft()
        if n == 1:
            print(count)
            break
        if n % 3 == 0:
            if visited[n // 3] == 0:
                visited[n // 3] = 1
                queue.append((n//3, count+1))
        if n % 2 == 0:
            if visited[n // 2] == 0:
                visited[n // 2] = 1
                queue.append((n//2, count+1))
        if visited[n - 1] == 0:
            visited[n - 1] = 1
            queue.append((n-1, count+1))


queue.append((N, 0))
bfs()