N = int(input())

visited = [-1] * (N+1)
visited[0] = 0
visited[1] = 1

def dp(n):
    if n == N:
        print(visited[n-1] + visited[n-2])
    else:
        visited[n] = visited[n-1] + visited[n-2]
        dp(n+1)


if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    dp(2)