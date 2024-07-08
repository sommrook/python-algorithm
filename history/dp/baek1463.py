from collections import deque
import sys
sys.setrecursionlimit(10**6)

N = int(input())

visited = [0] * (N+1)

queue = deque()

def bottom_up(n):
    for i in range(2, n+1):
        visited[i] = visited[i-1] + 1
        if i % 3 == 0:
            visited[i] = min(visited[i//3]+1, visited[i])
        if i % 2 == 0:
            visited[i] = min(visited[i//2]+1, visited[i])


def top_down(n):
    pass


bottom_up(N)
print(visited[N])