N = int(input())

stairs = [int(input()) if i != 0 else 0 for i in range(N+1)]
visited = [0] * (N+1)

max_count = 0
def bfs(n):
    # 내가(n) 다음에 어디를 밟을지 선택
    global max_count
    if n == N:
        max_count = max(visited[n], max_count)
    elif 2 <= n < N:
        if visited[n - 1] == 0 or visited[n] == 0:
            if n+1 <= N:
                visited[n + 1] = visited[n] + stairs[n + 1]
                bfs(n + 1)
                visited[n + 1] = 0
        if n + 2 <= N:
            visited[n + 2] = visited[n] + stairs[n + 2]
            bfs(n + 2)
            visited[n + 2] = 0
    elif n == 1 or n == 0:
        if n+1 <= N:
            visited[n+1] = visited[n] + stairs[n+1]
            bfs(n+1)
            visited[n+1] = 0
        if n+2 <= N:
            visited[n+2] = visited[n] + stairs[n+2]
            bfs(n+2)
            visited[n+2] = 0


bfs(0)
print(max_count)