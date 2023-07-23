Computer = int(input())
N = int(input())

"""
graph는 양방향임을 잊지 말자!

반례)
3
2
1 3
2 3

list의 index를 활용하는 방법을 사용해보자
ex)
graph = [[] for i in range(N+1)]

graph[c1].append(c2)
graph[c2].append(c1)
"""

# graph = dict()
graph = [[] for i in range(Computer+1)]
search = dict()
for i in range(N):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)
    # if c1 not in graph:
    #     graph[c1] = [c2]
    # else:
    #     graph[c1].append(c2)
    # if c2 not in graph:
    #     graph[c2] = [c1]
    # else:
    #     graph[c2].append(c1)

def dfs(i):
    # 자식에 대한것만
    for j in graph[i]:
        if j not in search and j != 1:
            search[j] = 1
            dfs(j)


dfs(1)
print(len(search))

